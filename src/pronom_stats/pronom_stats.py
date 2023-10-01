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
from fastapi.responses import RedirectResponse

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


async def _insert_version(version: str, summary: str):
    """Deleteme"""
    ins = f"insert into pronom (version, summary) values ('{version}', '{summary}');"
    app.cur.execute(ins)
    app.cur.execute("commit;")
    return


def _load_config():
    """Ensure the config is properly loaded."""
    load_dotenv(ENV_FILE)
    try:
        os.environ["SERVER_AUTH"]
    except KeyError as err:
        logging.error("environment needs configuring: %s", err)
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


@app.get("/pronom_version", tags=[TAG_PRONOM])
async def get_pronom_version():
    """Retrieve the PRONOM version from the database."""
    res = app.cur.execute("select version from pronom order by rowid desc limit 1;")
    res = res.fetchone()
    return res[0]


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
        default=8000,
    )

    args = parser.parse_args()

    logger.info(
        "attempting API startup, try setting `--port` arg if there are any issues"
    )

    import_str = "pronom_stats"
    try:
        importlib.import_module(import_str)
        import_str = f"{import_str}:app"
    except ModuleNotFoundError:
        import_str = "src.pronom_stats.pronom_stats:app"
        logger.info("importing from %s", import_str)

    uvicorn.run(
        import_str,
        host="0.0.0.0",
        port=int(args.port),
        access_log=False,
        log_level="info",
        reload=False,
    )


if __name__ == "__main__":
    main()
