"""Rudimentary script to check PRONOM updates and update the
stats server.
"""

# pylint: disable=R0801

import argparse
import asyncio
import hashlib
import json
import logging
import os
import sys
import time
from typing import Final

from dotenv import load_dotenv

try:
    from src.pronom_tools import pronom_tools
except ModuleNotFoundError:
    from pronom_tools import pronom_tools

import requests

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

load_dotenv(ENV_FILE)


def _get_auth():
    """Retrieve the authentication information from the environment."""
    system_pass = None
    try:
        system_pass = os.environ["SERVER_AUTH"]
    except KeyError as err:
        logging.error("environment needs configuring: %s", err)
        sys.exit(1)
    digest = hashlib.sha256()
    digest.update(system_pass.strip().encode())
    return digest.hexdigest()


def _get_api_addr():
    """Get the address of the API server."""
    server_addr = ""
    try:
        server_addr = os.environ["SERVER_ADDR"]
    except KeyError as err:
        logging.error("environment needs configuring: %s", err)
        sys.exit(1)
    return server_addr


def store_pronom_summary(data: str):
    """Store the PRONOM summary."""
    headers = {}
    headers["auth"] = _get_auth()
    server_addr = _get_api_addr()
    try:
        resp = requests.put(
            f"{server_addr}/pronom_summary",
            data=json.dumps(data),
            headers=headers,
            timeout=30,
        )
        if resp.status_code != 200:
            logger.error("error storing PRONOM data: %s", resp)
            sys.exit(1)
    except requests.exceptions.ConnectionError as err:
        logger.error("unable to connect to database: %s", err)
        sys.exit(1)
    logger.info("PRONOM data stored")


async def cron_main():
    """PRONOM cron functions."""

    parser = argparse.ArgumentParser(
        prog="PRONOM cron",
        description="Rudimentary handler for checking for PRONOM updates and updating the stats DB",
        epilog="for more information visit https://ffdev.info/",
    )

    parser.add_argument(
        "--init",
        "-i",
        help="initialize the database (only needed on first run)",
        required=False,
        action="store_true",
    )

    args = parser.parse_args()

    if args.init:
        logger.info("initializing database")
        data = await pronom_tools.get_summary(clean=True)
        store_pronom_summary(data=data)
        sys.exit()
    rel = pronom_tools.check_for_release()
    if rel:
        data = await pronom_tools.get_summary(clean=True)
        store_pronom_summary(data=data)


def main():
    """Primary entry point for this script."""
    asyncio.run(cron_main())


if __name__ == "__main__":
    main()
