"""Export PRONOM XML.

Originally: https://github.com/ffdev-info/pronom-xml-export
"""

# pylint: disable=R0801

import argparse
import logging
import multiprocessing
import os
import sys
import time
from pathlib import Path
from typing import Final

import requests
from tenacity import retry, wait_exponential

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


class PronomExportException(Exception):
    """Exception to raise when there is a problem with this script."""


# folder in which to place the download output
EXPORT_DIR: Final[str] = "pronom-export"


# url through which to access Pronom data...
BASE_URL: Final[str] = "https://www.nationalarchives.gov.uk/PRONOM/"


def check_record(ffb: str) -> bool:
    """Ensure that we're downloading an XML record.

    NB. ffb == "first fourteen bytes"
    """
    xml_string: Final[str] = "<?xml version="  # Expected BOF bytes from XML export.
    if ffb == xml_string:
        return True
    return False


@retry(wait=wait_exponential(multiplier=1, min=4, max=10))
def download_and_save_puid(puid_filename_pair: tuple) -> None:
    """Perform the HTTP request and save routine to save the
    PRONOM record to disk.
    """
    puid_url, file_name = puid_filename_pair
    header = {"User-Agent": "exponentialDK-PRONOM-Export/0.0.0"}
    logger.info(puid_url)
    request = requests.get(puid_url, timeout=30, headers=header)
    test_string = request.text[:14]
    if not check_record(test_string):
        logger.info("not writing record: %s (%s)", file_name, test_string)
        return
    with open(file_name, "w", encoding="utf-8") as fmt_record:
        fmt_record.write(request.text)
    time.sleep(0.5)
    return


def get_x_fmt_range() -> int:
    """x-fmt records should never be added to by the PRONOM team. The
    number is static at 455.

    If they are ever added to, this code is suboptimal to handle that
    so this will need to be updated manually.
    """
    x_fmt_limit: Final[int] = 455
    return x_fmt_limit + 1


def export_pronom_data(fmt_range: int = None):
    """Export PRONOM data and write locally"""

    if not fmt_range:
        raise PronomExportException("fmt puid range is not set")

    x_fmt = ("x-fmt", get_x_fmt_range())
    fmt = ("fmt", fmt_range)

    logger.info("downloading: %s %s", fmt, x_fmt)

    for puid_type, puid_range in [fmt, x_fmt]:
        # Create a directory to write to.
        puid_type_url = f"{BASE_URL}{puid_type}/"
        new_dir = Path(os.path.join(EXPORT_DIR, puid_type))
        new_dir.mkdir(parents=True, exist_ok=True)

        # Create a list of puid urls and filenames to save the outputs to.
        puid_filename_pairs = []
        for idx in range(1, puid_range):
            puid_url = f"{puid_type_url}{idx}.xml"
            file_name = new_dir / Path(f"{puid_type}{idx}.xml")
            puid_filename_pairs.append((puid_url, file_name))

        # Download PRONOM data.
        with multiprocessing.Pool() as pool:
            pool.map(download_and_save_puid, puid_filename_pairs)


def main():
    """Primary entry point for this script."""

    parser = argparse.ArgumentParser(
        prog="PRONOM Export",
        description="A method to export PRONOM XML records for further processing",
        epilog="for more information visit https://ffdev.info/",
    )

    parser.add_argument(
        "--fmt-range",
        "-f",
        help="current max record no. of fmt/puids (x-fmts are constant at 455)",
        required=False,
        type=int,
    )

    args = parser.parse_args()
    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit()
    time_start = time.perf_counter()  # time script execution time roughly...
    export_pronom_data(args.fmt_range)
    logger.info("execution time: %s seconds", str(time.perf_counter() - time_start))


if __name__ == "__main__":
    main()
