"""PRONOM stats server to be hosted on ffdev.info.

The app allows us to record statistics about PRONOM that can then be
used to guide signature development work.

The goal of this API is to have a "put" endpoing that can receive
information about the latest information available on the PRONOM
server.

Whether this goal is required, schauen wir mal.

    `uvicorn pronom_stats:app --reload`

The database for this app is stored in `/var/tmp/pronom-stats.db`. The
location can be cleared manually if necessary. Data will persist at
reboot time otherwise. It's not hugely important to the functioning
of this app.
"""

# pylint: disable=E1101,R0801

import argparse
import functools
import hashlib
import importlib
import json
import logging
import os
import sqlite3
import time
from contextlib import asynccontextmanager
from typing import Annotated, Final

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Header, HTTPException, Request, status
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


@asynccontextmanager
async def lifespan(context: FastAPI):
    """Load the database connection for the life of the app.s"""
    _load_config()
    con = sqlite3.connect(os.path.join("/var", "tmp", "pronom-stats.db"))
    context.cur = con.cursor()
    await init_db(context.cur)
    yield


#### API Entry Points ####

# API description.
API_DESCRIPTION: Final[str] = "ffdev.info PRONOM API"

# OpenAPI tags delineating the documentation.
TAG_PRONOM: Final[str] = "pronom"

# Metadata for each of the tags in the OpenAPI specification. To order
# their display on the page, order the tags in this block.
tags_metadata = [
    {
        "name": TAG_PRONOM,
        "description": "Manage PRONOM data",
    },
]

app = FastAPI(
    title="api.pronom.ffdev.info",
    description=API_DESCRIPTION,
    version="0.0.1",
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
                "xpuid_const": "x-fmt/455",
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


@app.get("/pronom_version", tags=[TAG_PRONOM], response_class=HTMLResponse)
async def get_pronom_version() -> str:
    """Retrieve the PRONOM version from the database."""
    res = app.cur.execute("select version from pronom order by rowid desc limit 1;")
    res = res.fetchone()
    return res[0]


@functools.cache
def _get_summary() -> dict:
    """Return the PRONOM summary from the database."""
    res = app.cur.execute("select summary from pronom order by rowid desc limit 1;")
    res = res.fetchone()
    return json.loads(res[0])


@app.get("/records_count", tags=[TAG_PRONOM])
async def get_complete_records_count():
    """Retrieve the PRONOM version from the database."""
    summary = _get_summary()
    return len(summary.get("pronom_data", []))


@app.get("/complete_description_count")
async def get_complete_descriptions_count():
    """Retrieve the number of PRONOM descriptions with status complete."""
    summary = _get_summary()
    complete = [
        item
        for item in summary.get("pronom_data", [])
        if item["description"] == "complete"
    ]
    return len(complete)


@app.get("/incomplete_description_count")
async def get_incomplete_descriptions_count():
    """Retrieve the number of PRONOM descriptions with status complete."""
    summary = _get_summary()
    complete = [
        item
        for item in summary.get("pronom_data", [])
        if item["description"] != "complete"
    ]
    return len(complete)


@app.get("/signature_count")
async def get_signatures_count():
    """Retrieve the number of PRONOM descriptions with status complete."""
    summary = _get_summary()
    signatures = [
        item for item in summary.get("pronom_data", []) if item["signature"] is True
    ]
    return len(signatures)


@app.get("/requires_signature_count")
async def get_requires_signatures_count():
    """Retrieve the number of PRONOM descriptions where signatures are
    still required.
    """
    summary = _get_summary()
    signatures = [
        item for item in summary.get("pronom_data", []) if item["signature"] is not True
    ]
    return len(signatures)


@app.get("/signature_files", response_class=HTMLResponse)
async def get_signature_files():
    """List the signature files associated with the latest PRONOM
    release.
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


@app.get("/incomplete_descriptions", response_class=HTMLResponse)
async def get_incomplete_descriptions():
    """Retrieve the number of PRONOM descriptions with status complete."""
    summary = _get_summary()
    complete = [
        item
        for item in summary.get("pronom_data", [])
        if item["description"] != "complete"
    ]
    return _make_formatted_list_from_summary_items(complete)


@app.get("/requires_signatures", response_class=HTMLResponse)
async def get_requires_signatures():
    """Retrieve the number of PRONOM descriptions with status complete."""
    summary = _get_summary()
    signatures = [
        item for item in summary.get("pronom_data", []) if item["signature"] is not True
    ]
    return _make_formatted_list_from_summary_items(signatures)


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
        reload=True,
    )


if __name__ == "__main__":
    main()
