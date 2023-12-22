"""Tools to help with the PRONOM release pipeline.

Summary outputs look as follows:

```json
    {
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
```

For each PRONOM record `container signautre` is optional, if either
`signature` or `container_signature` is `True` the record is considered
to have a signature for identification.

Descriptions have the following statuses:

```python
    DEPRECATED: Final[str] = "deprecated"
    OUTLINE: Final[str] = "outline"
    COMPLETE: Final[str] = "complete"
```
s
Assumption: Container signature file appears online before the release
notes. If it doesn't then this information will be out of sync from
one another.
"""

import argparse
import asyncio
import hashlib
import json
import logging
import os
import re
import sys
import time
import xml.etree.ElementTree as etree
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Final, Union

import requests
from dotenv import load_dotenv

from .version import get_version

try:
    from src.pronom_export.pronom_xml_export import export_pronom_data
    from src.pronom_summary.pronom_summary import parse_pronom
except ModuleNotFoundError:
    from pronom_export.pronom_xml_export import export_pronom_data
    from pronom_summary.pronom_summary import parse_pronom


ENV_FILE: Final[str] = "pronom.env"

load_dotenv(ENV_FILE, verbose=True)

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


RELEASE_NOTE_URL: Final[
    str
] = "https://www.nationalarchives.gov.uk/aboutapps/pronom/release-notes.xml"


USER_AGENT: Final[str] = "pronom-tools/0.0.0"


class PronomToolsException(Exception):
    """Exception to raise if there's an error in the workflow."""


CDN_BASE: Final[str] = "https://cdn.nationalarchives.gov.uk/documents/"
RELEASE_ARCHIVE = (
    "https://www.nationalarchives.gov.uk/aboutapps/pronom/droid-signature-files.htm"
)
CONTAINER_UPDATE_URL: Final[
    str
] = "https://www.nationalarchives.gov.uk/pronom/container-signature.xml"


@dataclass
class ReleaseSummary:
    """Release summary object."""

    date: str
    latest_puid: str
    version: str
    release_notes: str
    sig_file: str = ""
    container_sig: str = ""
    xpuid_const: str = "x-fmt/455"

    @staticmethod
    def _get_container_formatted_date(date: str):
        """Return a date formatted to container-signature-file
        specifications.
        """
        date_format = "%a, %d %b %Y %H:%M:%S GMT"
        date_obj = datetime.strptime(date, date_format)
        return datetime.strftime(date_obj, "%Y%m%d")

    def _get_container_date(self):
        """Get the latest container signature file date from the
        canonical update location. Last-modified-date is used to set
        this in DROID itself.
        """
        http_headers = requests.head(
            CONTAINER_UPDATE_URL, timeout=30, headers=make_headers()
        )
        if not http_headers.status_code == 200:
            raise PronomToolsException("error reading release headers")
        http_last_modified_date = http_headers.headers.get("Last-modified")
        http_date = self._get_container_formatted_date(http_last_modified_date)
        return http_date

    def make_sig_file_url(self) -> str:
        """Construct a URL to the standard signature file for the given
        release summary.

        Example: `https://cdn.nationalarchives.gov.uk/documents/DROID_SignatureFile_V116.xml`
        """
        file_name = f"{CDN_BASE}DROID_SignatureFile_V{self.version.lower().replace('v', '')}.xml"
        self.sig_file = file_name
        return file_name

    def make_container_sig_file_url(self) -> str:
        """Construct a URL to the container signature file for the
        given release summary.

        Example: `https://cdn.nationalarchives.gov.uk/documents/container-signature-20231127.xml`
        """
        file_name = f"{CDN_BASE}container-signature-{self._get_container_date()}.xml"
        self.container_sig = file_name
        return file_name

    def get_container_name(self) -> str:
        """Return just the container signature file name."""
        return self.container_sig.replace(CDN_BASE, "")


def download_container(rel: ReleaseSummary) -> str:
    """Download a container signature file and return the signature file
    name for use in later functions.

    Example release summary:

    ```json
        {
            "date": "2023-11-23",
            "puid": "fmt/1924",
            "version": "V116",
            "sig_file": "https://cdn.nationalarchives.gov.uk/documents/DROID_SignatureFile_V116.xml",
            "container_sig": "https://cdn.nationalarchives.gov.uk/documents/container-signature-20231127.xml"
        }
    ```
    """
    res = requests.get(rel.container_sig, timeout=30)
    file_name = rel.container_sig.split(CDN_BASE, 1)[1]
    with open(file_name, "w", encoding="utf-8") as sig_file:
        sig_file.write(res.text)
    return file_name


def download_standard(rel: ReleaseSummary) -> str:
    """Download a standard signature file and return the signature file
    name for use in later functions.

    Example release summary:

    ```json
        {
            "date": "2023-11-23",
            "puid": "fmt/1924",
            "version": "V116",
            "sig_file": "https://cdn.nationalarchives.gov.uk/documents/DROID_SignatureFile_V116.xml",
            "container_sig": "https://cdn.nationalarchives.gov.uk/documents/container-signature-20231127.xml"
        }
    ```
    """
    res = requests.get(rel.sig_file, timeout=30)
    file_name = rel.sig_file.split(CDN_BASE, 1)[1]
    with open(file_name, "w", encoding="utf-8") as sig_file:
        sig_file.write(res.text)
    return file_name


def perform_export(max_puid: int):
    """Export PRONOM xml records."""
    export_pronom_data(fmt_range=max_puid + 1)


def make_headers() -> dict:
    """Create a HTTP header object for the different http requests
    in this script.
    """
    return {"user-agent": USER_AGENT}


def replace_day_suffix(day: str):
    """Replace suffixes in day strings, e.g. 2nd, 3rd.

    Source: https://stackoverflow.com/a/21496318
    """
    return re.sub(r"(\d)(st|nd|rd|th)", r"\1", day)  # noqa, codespell


def parse_signature_file_string(sig_file: str) -> str:
    """Parse the signature file string and return a version number.

    Examples:

        * DROID_SignatureFile_V114.xml
        * DROID_SignatureFile_V112.xml
        * DROID_SignatureFile_V111.xml
        * DROID_SignatureFile_V110.xml
        * DROID_SignatureFile_V109.xml

    """
    return sig_file.replace("DROID_SignatureFile_", "").replace(".xml", "")


def parse_release_date(date: str) -> str:
    """Parse PRONOM release dates."""
    date_str = replace_day_suffix(date.strip())
    date_format = "%d %B %Y"
    date_obj = datetime.strptime(date_str, date_format)
    return str(date_obj.date())


def parse_newest_record_id(records: etree.Element) -> str:
    """Retrieve the newest record identifier from the signature
    file.
    """
    formats = records.findall("format")
    return f"fmt/{formats[len(formats) - 1].find('puid').text}"


def parse_http_date(date: str) -> datetime:
    """Parse the HTTP dates from the release notes."""
    date_format = "%a, %d %b %Y %H:%M:%S GMT"
    date_obj = datetime.strptime(date, date_format)
    return date_obj


def parse_release_xml(release_xml: str) -> (str, str, str):
    """Parse the PRONOM release notes XML.

    We need three pieces of information from here, the release date and
    the latest PRONOM record identifier and the version of the signature
    file.
    """
    root = etree.fromstring(release_xml.strip())
    # Most recent release will always be the first in the Release Note XML.
    latest = root.find("release_note")
    date = latest.find("release_date")
    release_outline = latest.find("release_outline")
    signature_file_name = latest.find("signature_filename")
    release_date = parse_release_date(date.text)
    newest_record = parse_newest_record_id(release_outline)
    signature_version = parse_signature_file_string(signature_file_name.text)
    summary = ReleaseSummary(
        release_date,
        newest_record,
        signature_version,
        RELEASE_NOTE_URL,
    )
    summary.make_sig_file_url()
    summary.make_container_sig_file_url()
    return summary


def check_release_headers() -> (bool, datetime):
    """Check the HTTP headers of the release note to see if there is
    a newer date than we have recorded."""
    http_headers = requests.head(RELEASE_NOTE_URL, timeout=30, headers=make_headers())
    if not http_headers.status_code == 200:
        raise PronomToolsException("error reading release headers")
    http_last_modified_date = http_headers.headers.get("Last-modified")
    http_date = parse_http_date(http_last_modified_date)
    return (http_date.date() == datetime.now().date(), http_date)


def check_for_release() -> Union[None | ReleaseSummary]:
    """Check for a new release of PRONOM."""
    today, http_date = check_release_headers()
    if not today:
        logger.info(
            "last updated '%s' is not today skipping release check", http_date.date()
        )
        return None
    resp = requests.get(RELEASE_NOTE_URL, timeout=30, headers=make_headers())
    return parse_release_xml(resp.text)


def check_existing() -> Union[None | ReleaseSummary]:
    """Return information about the existing pronom release."""
    resp = requests.get(RELEASE_NOTE_URL, timeout=30, headers=make_headers())
    return parse_release_xml(resp.text)


def _dump_rel(rel: ReleaseSummary) -> str:
    """Convenience function to enable printing of release information
    as a dictionary.
    """
    return json.dumps(asdict(rel), indent=2)


async def get_summary(clean: bool = False) -> dict:
    """Perform the get summary dance."""
    rel = check_existing()
    max_puid = int(rel.latest_puid.lower().replace("fmt/", ""))
    if not Path("pronom-export").exists() or clean:
        perform_export(max_puid)
    sig_file = download_container(rel)
    res = await parse_pronom("pronom-export", sig_file)
    rel_augmented = asdict(rel)
    rel_augmented["pronom_data"] = res
    return rel_augmented


async def store_summary():
    """Store the PRONOM summary in the database."""
    summary = await get_summary()
    store_pronom_summary(summary)


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


async def pronom_tools():
    """Run the PRONOM tooling."""
    parser = argparse.ArgumentParser(
        prog="PRONOM tools",
        description="Provides helper functions for PRONOM releases",
        epilog="for more information visit https://ffdev.info/",
    )

    parser.add_argument(
        "--new-release",
        "-n",
        help="check whether there was a new PRONOM release",
        required=False,
        action="store_true",
    )

    parser.add_argument(
        "--check-existing",
        "-e",
        help="return information about the existing pronom release",
        required=False,
        action="store_true",
    )

    parser.add_argument(
        "--summary",
        "-s",
        help="summarize existing PRONOM data",
        required=False,
        action="store_true",
    )

    parser.add_argument(
        "--store",
        "-st",
        help="store existing PRONOM summary (ensure that an existing pronom-stats server is running)",
        required=False,
        action="store_true",
    )

    parser.add_argument(
        "--clean-and-summary",
        "-c",
        help="download and output any existing PRONOM data (deletes existing `pronom-export` folder)",
        required=False,
        action="store_true",
    )

    parser.add_argument(
        "--download-container",
        "-dc",
        help="download container signature file",
        required=False,
        action="store_true",
    )

    parser.add_argument(
        "--download-signature",
        "-ds",
        help="download standard signature file",
        required=False,
        action="store_true",
    )

    parser.add_argument(
        "--version",
        "-v",
        help="return version information",
        required=False,
        action="store_true",
    )

    args = parser.parse_args()

    if args.new_release:
        rel = check_for_release()
        if not rel:
            sys.exit(1)
        print(_dump_rel(rel))

    if args.check_existing:
        rel = check_existing()
        print(_dump_rel(rel))
        sys.exit()

    if args.version:
        print(get_version())
        sys.exit()

    if args.summary or args.clean_and_summary:
        res = await get_summary(args.clean_and_summary)
        print(json.dumps(res, indent=2))
        sys.exit()

    if args.store:
        res = await store_summary()
        sys.exit()

    if args.download_container:
        rel = check_existing()
        sig_file = download_container(rel)
        print("container sig output to:", Path(sig_file).resolve())
        sys.exit()

    if args.download_signature:
        rel = check_existing()
        sig_file = download_standard(rel)
        print("container sig output to:", Path(sig_file).resolve())
        sys.exit()

    parser.print_help()


def main() -> None:
    """Primary entry point for this script."""
    asyncio.run(pronom_tools())


if __name__ == "__main__":
    main()
