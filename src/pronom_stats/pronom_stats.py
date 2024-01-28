"""PRONOM stats server to be hosted on ffdev.info.

The app allows us to record statistics about PRONOM that can then be
used to guide signature development work.

The goal of this API is to have a "put" endpoing that can receive
information about the latest information available on the PRONOM
server.

Whether this goal is required, schauen wir mal.

    `uvicorn pronom_stats:app --reload`

The database for this app is configured by the DATABASE_PATH environment
variable.
"""

# pylint: disable=E1101,R0801

import argparse
import hashlib
import importlib
import json
import logging
import os
import sqlite3
import time
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Annotated, Final

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Header, HTTPException, Request, Response, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, RedirectResponse

# Set up logging.
logging.basicConfig(
    format="%(asctime)-15s %(levelname)s :: %(filename)s:%(lineno)s:%(funcName)s() :: %(message)s",  # noqa: E501
    datefmt="%Y-%m-%d %H:%M:%S",
    level="INFO",
    handlers=[
        logging.StreamHandler(),
    ],
)

# Format logs using UTC time.
logging.Formatter.converter = time.gmtime


logger = logging.getLogger(__name__)

ENV_FILE: Final[str] = "pronom.env"
DEPRECATED: Final[str] = "deprecated"


async def init_db(cur: sqlite3.Cursor):
    """Initialize the database if it doesn't exist."""
    try:
        cur.execute("CREATE TABLE pronom(version, summary)")
    except sqlite3.OperationalError:
        # database is already setup.
        pass


def _escape_ins(ins: str) -> str:
    """Provides a way to escape the data we're inserting. It's a bit
    of a hack. First created to handle single-quotes but will
    potentially be needed for other character types.
    """
    return ins.replace("'", "")


async def _insert_version(version: str, summary: str):
    """Deleteme"""
    summary = _escape_ins(summary)
    ins = f"insert into pronom (version, summary) values ('{version}', '{summary}');"
    app.cur.execute(ins)
    app.cur.execute("commit;")
    return


def _load_config():
    """Ensure the config is properly loaded."""
    load_dotenv(ENV_FILE, override=False, verbose=True)
    try:
        os.environ["SERVER_AUTH"]
    except KeyError as err:
        logging.error(
            "environment needs configuring: %s (e.g. SERVER_AUTH='badf00d')", err
        )
        raise err
    try:
        os.environ["DATABASE_PATH"]
    except KeyError as err:
        logging.error(
            "environment needs configuring: %s (e.g. DATABASE_PATH='/path/to/database')",
            err,
        )
        raise err


@asynccontextmanager
async def lifespan(context: FastAPI):
    """Load the database connection for the life of the app.s"""
    _load_config()
    db_path = Path(os.environ["DATABASE_PATH"])
    logger.info("pronom database path: %s", db_path)
    con = sqlite3.connect(db_path)
    context.cur = con.cursor()
    await init_db(context.cur)
    yield


#### API Entry Points ####

# API description.
API_DESCRIPTION: Final[str] = "ffdev.info PRONOM API"

# OpenAPI tags delineating the documentation.
TAG_PRONOM: Final[str] = "pronom"
TAG_STATISTICS: Final[str] = "statistics"
TAG_REPORTS: Final[str] = "reports"
TAG_HTMX: Final[str] = "htmx"

# Metadata for each of the tags in the OpenAPI specification. To order
# their display on the page, order the tags in this block.
tags_metadata = [
    {
        "name": TAG_PRONOM,
        "description": "Manage PRONOM data",
    },
    {
        "name": TAG_STATISTICS,
        "description": "PRONOM statistics",
    },
    {
        "name": TAG_REPORTS,
        "description": "PRONOM reports",
    },
    {
        "name": TAG_HTMX,
        "description": "Endpoints designed to be used with HTML elements",
    },
]

app = FastAPI(
    title="api.pronom.ffdev.info",
    description=API_DESCRIPTION,
    version="1.0.0",
    contact={
        "Github": "https://github.com/ross-spencer/",
    },
    openapi_tags=tags_metadata,
    lifespan=lifespan,
)

origins = [
    "http://127.0.0.1:26001",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["X-Content-type"],
)


@app.get("/", include_in_schema=False)
def redirect_root_to_docs():
    """Redirect a user calling the API root '/' to the API
    documentation.
    """
    return RedirectResponse(url="/docs")


def _get_summary() -> dict:
    """Return the PRONOM summary from the database."""
    res = app.cur.execute("select summary from pronom order by rowid desc limit 1;")
    res = res.fetchone()
    return json.loads(res[0])


@app.get("/pronom_summary", tags=[TAG_PRONOM])
async def get_pronom_summary():
    """Retrieve the PRONOM summary information from the database.

    Result should looks something like as follows:

    ```json
        {
            "version": "v116",
            "summary": {
                "date": "2023-11-23",
                "latest_puid": "fmt/1924",
                "version": "V116",
                "sig_file": "https://cdn.nationalarchives.gov.uk/documents/DROID_SignatureFile_V116.xml",
                "container_sig": "https://cdn.nationalarchives.gov.uk/documents/container-signature-20231127.xml",
                "x_puid_const": "x-fmt/455",
                "pronom_data": [
                    {
                        "name": "Broadcast WAVE 0 Generic",
                        "description": "complete",
                        "signature": true,
                        "identifier": "fmt/1"
                    },
                    {
                        "name": "Microsoft Word for Macintosh Document 3.0",
                        "description": "complete",
                        "signature": true,
                        "identifier": "x-fmt/1"
                    }
                ]
            }
        }
    ```
    """
    res = app.cur.execute(
        "select version, summary from pronom order by rowid desc limit 1;"
    )
    res = res.fetchone()
    ret = {}
    ret["version"] = res[0]
    ret["summary"] = json.loads(res[1])
    return ret


@app.get("/pronom_summary_csv", tags=[TAG_REPORTS])
async def get_pronom_summary_csv():
    """Return a simplified PRONOM summary as a CSV.

    Example using the Rust-based XSV tool on Linux:

    ```sh
        curl -sX 'GET' 'https://api.ffdev.info/pronom_summary_csv' \\n
            -H 'accept: application/json' | xsv table | less
    ```
    """
    res = _get_summary()
    pronom_data = res.get("pronom_data", [])
    if not pronom_data and not isinstance(pronom_data, list):
        return {"error": "problem retrieving PRONOM summary"}
    headers = pronom_data[0].keys()
    rows = ""
    for data in pronom_data:
        row = ",".join(f"{value}" for value in data.values())
        rows = f"{rows}\n{row}"
    headers = ",".join(headers)
    res = f"{headers}{rows}\n"
    return Response(content=res, media_type="text/csv")


@app.get("/pronom_version", tags=[TAG_PRONOM], response_class=HTMLResponse)
async def get_pronom_version() -> str:
    """Retrieve the PRONOM version from the database."""
    res = app.cur.execute("select version from pronom order by rowid desc limit 1;")
    res = res.fetchone()
    return res[0]


@app.get("/records_count", tags=[TAG_STATISTICS])
async def get_complete_records_count():
    """Retrieve the PRONOM version from the database."""
    summary = _get_summary()
    return len(summary.get("pronom_data", []))


@app.get("/complete_description_count", tags=[TAG_STATISTICS])
async def get_complete_descriptions_count():
    """Retrieve the number of PRONOM descriptions with status complete."""
    summary = _get_summary()
    complete = [
        item
        for item in summary.get("pronom_data", [])
        if item["description"] == "complete"
    ]
    return len(complete)


@app.get("/incomplete_description_count", tags=[TAG_STATISTICS])
async def get_incomplete_descriptions_count():
    """Retrieve the number of PRONOM descriptions with status complete."""
    summary = _get_summary()
    complete = [
        item
        for item in summary.get("pronom_data", [])
        if item["description"] != "complete" and item["description"] != DEPRECATED
    ]
    return len(complete)


@app.get("/signature_count", tags=[TAG_STATISTICS])
async def get_signatures_count():
    """Retrieve the number of PRONOM descriptions with status complete."""
    summary = _get_summary()
    signatures = [
        item
        for item in summary.get("pronom_data", [])
        if item["signature"] is True and item["description"] != DEPRECATED
    ]
    return len(signatures)


@app.get("/requires_signature_count", tags=[TAG_STATISTICS])
async def get_requires_signatures_count():
    """Retrieve the number of PRONOM descriptions where signatures are
    still required.
    """
    summary = _get_summary()
    signatures = [
        item
        for item in summary.get("pronom_data", [])
        if item["signature"] is not True and item["description"] != DEPRECATED
    ]
    return len(signatures)


@app.get("/signature_files", tags=[TAG_PRONOM])
async def get_signature_files():
    """List the signature files associated with the latest PRONOM
    release. Format the output as HTML.
    """
    summary = _get_summary()
    standard_sig = summary.get("sig_file")
    container_sig = summary.get("container_sig")
    return {
        "standard signature": standard_sig,
        "container signature": container_sig,
    }


@app.get("/signature_files_hx", response_class=HTMLResponse, tags=[TAG_HTMX])
async def get_signature_files_hx():
    """List the signature files associated with the latest PRONOM
    release. Format the output as HTML.
    """
    summary = _get_summary()
    standard_sig = summary.get("sig_file")
    container_sig = summary.get("container_sig")
    return (
        f"<br>"
        f"<ul>"
        f"<li>Standard signature file: <a href='{standard_sig}'>{standard_sig}</a></li>"
        f"<li>Container signature file: <a href='{container_sig}'>{container_sig}</a></li>"
        f"</ul>"
    )


def _make_url_from_identifier(identifier: str) -> str:
    """Make a PRONOM URL from its inentifier."""
    url_pattern = "https://www.nationalarchives.gov.uk/PRONOM/"
    return f"<a href='{url_pattern}{identifier}'>{identifier}</a>"


def _make_formatted_list_from_summary_items(summary_objs: list) -> str:
    """Make a formatted list from a list of summary items.

    Example item:

    ```json
            {
            "name": "Microsoft Word for Macintosh Document 3.0",
            "description": "incomplete",
            "signature": true,
            "identifier": "x-fmt/1"
        }
    ```
    """
    list_obj = [
        f"{item['name']} ({_make_url_from_identifier(item['identifier'])})<br>"
        for item in summary_objs
    ]
    return "".join(list_obj)


@app.get("/incomplete_descriptions", tags=[TAG_REPORTS])
async def get_incomplete_descriptions():
    """Retrieve the number of PRONOM descriptions with status complete."""
    summary = _get_summary()
    complete = [
        item
        for item in summary.get("pronom_data", [])
        if item["description"] != "complete" and item["description"] != DEPRECATED
    ]
    return complete


@app.get("/incomplete_descriptions_hx", response_class=HTMLResponse, tags=[TAG_HTMX])
async def get_incomplete_descriptions_hx():
    """Retrieve the number of PRONOM descriptions with status complete."""
    summary = _get_summary()
    complete = [
        item
        for item in summary.get("pronom_data", [])
        if item["description"] != "complete" and item["description"] != DEPRECATED
    ]
    return _make_formatted_list_from_summary_items(complete)


@app.get("/requires_signatures", tags=[TAG_REPORTS])
async def get_requires_signatures():
    """Retrieve the number of PRONOM descriptions with status complete."""
    summary = _get_summary()
    signatures = [
        item
        for item in summary.get("pronom_data", [])
        if item["signature"] is not True and item["description"] != DEPRECATED
    ]
    return signatures


@app.get("/requires_signatures_hx", response_class=HTMLResponse, tags=[TAG_HTMX])
async def get_requires_signatures_hx():
    """Retrieve the number of PRONOM descriptions with status complete."""
    summary = _get_summary()
    signatures = [
        item
        for item in summary.get("pronom_data", [])
        if item["signature"] is not True and item["description"] != DEPRECATED
    ]
    return _make_formatted_list_from_summary_items(signatures)


@app.get("/get_deprecated", tags=[TAG_REPORTS])
async def get_deprecated():
    """Retrieve the number of PRONOM descriptions with status complete."""
    summary = _get_summary()
    deprecated = [
        item
        for item in summary.get("pronom_data", [])
        if item["description"] == "deprecated" and item["description"] != DEPRECATED
    ]
    return deprecated


@app.get("/get_deprecated_count", tags=[TAG_STATISTICS])
async def get_deprecated_count():
    """Retrieve the number of PRONOM descriptions with status complete."""
    summary = _get_summary()
    deprecated = [
        item
        for item in summary.get("pronom_data", [])
        if item["description"] == DEPRECATED
    ]
    return len(deprecated)


@app.get("/get_deprecated_hx", response_class=HTMLResponse, tags=[TAG_HTMX])
async def get_deprecated_hx():
    """Retrieve the number of PRONOM descriptions with status complete."""
    summary = _get_summary()
    deprecated = [
        item
        for item in summary.get("pronom_data", [])
        if item["description"] == DEPRECATED
    ]
    return _make_formatted_list_from_summary_items(deprecated)


def _get_auth():
    """Retrieve the authentication information from the environment."""
    load_dotenv(ENV_FILE)
    system_pass = os.getenv("SERVER_AUTH")
    digest = hashlib.sha256()
    digest.update(system_pass.strip().encode())
    return digest.hexdigest()


@app.put("/pronom_summary", tags=[TAG_PRONOM])
async def put_summary(
    request: Request,
    auth: Annotated[str | None, Header()] = None,
):
    """Provides a mechanism to store the PRONOM version number.

    The so-called `auth` method in this function is a shot-to-medium
    term hack that allows the endpoint to be used locally.

    NB. The stakes are pretty low; if it's used even, letalone hacked
    we'll figure something more permanent out.
    """
    system_pass = _get_auth()
    logger.info(system_pass)
    if not system_pass or auth != system_pass.strip():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="incorrect auth token",
        )
    logger.info("auth OK")
    req = await request.json()
    version = req.get("version")
    summary = {}
    summary["summary"] = req
    await _insert_version(f"{version}", json.dumps(req))
    return {"message": "success"}


def main():
    """Primary entry point for this script."""

    parser = argparse.ArgumentParser(
        prog="pronom-stats",
        description="PRONOM Stats API",
        epilog="for more information visit https://ffdev.info/",
    )

    parser.add_argument(
        "--port",
        help="provide a port on which to run the app",
        required=False,
        default=26000,
    )

    parser.add_argument(
        "--reload",
        help="enable reload in development mode",
        required=False,
        default=False,
        action="store_true",
    )

    parser.add_argument(
        "--workers",
        help="enable more workers",
        required=False,
        default=1,
        type=int,
    )

    args = parser.parse_args()

    logger.info(
        "attempting API startup, try setting `--port` arg if there are any issues"
    )

    import_str = "src.pronom_stats.pronom_stats"
    try:
        importlib.import_module(import_str)
        import_str = f"{import_str}:app"
    except ModuleNotFoundError:
        import_str = "pronom_stats.pronom_stats:app"
        logger.info("importing from %s", import_str)

    logging.info("ensure that environment is configured (e.g. SERVER_AUTH='badf00d')")

    uvicorn.run(
        import_str,
        host="0.0.0.0",
        port=int(args.port),
        access_log=False,
        log_level="info",
        reload=args.reload,
        workers=args.workers,
    )


if __name__ == "__main__":
    main()
