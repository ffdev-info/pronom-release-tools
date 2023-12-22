"""Rudimentary script to check PRONOM updates and update the
stats server.
"""

# pylint: disable=R0801

import argparse
import asyncio
import logging
import sys
import time
from typing import Final

from dotenv import load_dotenv

try:
    from src.pronom_tools import pronom_tools
except ModuleNotFoundError:
    from pronom_tools import pronom_tools


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

load_dotenv(ENV_FILE, verbose=True)


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
        pronom_tools.store_pronom_summary(data=data)
        sys.exit()
    rel = pronom_tools.check_for_release()
    if rel:
        data = await pronom_tools.get_summary(clean=True)
        pronom_tools.store_pronom_summary(data=data)


def main():
    """Primary entry point for this script."""
    asyncio.run(cron_main())


if __name__ == "__main__":
    main()
