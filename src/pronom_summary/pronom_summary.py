"""Provide PRONOM record parsing capabilities."""

import asyncio
import json
import multiprocessing
import xml.etree.ElementTree as etree
from pathlib import Path
from typing import Final, Union
from xml.etree.ElementTree import ParseError

try:
    try:
        from src.pronom_tools import pronom_tools
    except ModuleNotFoundError:
        from pronom_tools import pronom_tools
except ImportError:
    # Module is likely being called from PRONOM tools and so doesn't
    # require this import.
    pass


NAMESPACES: Final[str] = {"pro": "http://pronom.nationalarchives.gov.uk"}
DEPRECATED: Final[str] = "deprecated"
OUTLINE: Final[str] = "outline"
COMPLETE: Final[str] = "complete"


class PRONOMException(Exception):
    """Exception to raise when there are errors with what is being
    processed.
    """


def summarize_container_xml(pronom_container_xml: Path) -> list[str]:
    """Return information about the container signature file from
    PRONOM.
    """
    try:
        tree = etree.parse(pronom_container_xml)
    except ParseError as err:
        raise PRONOMException(f"cannot parse xml: {pronom_container_xml}") from err
    root = tree.getroot()
    desc = root.find("FileFormatMappings")
    puids = []
    try:
        for item in desc:
            puids.append(item.attrib["Puid"])
    except KeyError as err:
        raise ProcessLookupError(
            f"cannot find puid attrib in {pronom_container_xml}: {err}"
        ) from err
    return puids


def get_puid(identifiers: list[etree.Element]) -> Union[str | None]:
    """Retrieve PUID from a list of identifiers"""
    for identifier in identifiers:
        identifier_type = identifier.find("pro:IdentifierType", NAMESPACES)
        if identifier_type.text != "PUID":
            continue
        return identifier.find("pro:Identifier", NAMESPACES).text
    return None


def process_desc(desc: str) -> str:
    """Identify outline and deprecated records. Simply return true
    if the description is complete.
    """

    # pylint: disable=R0911

    if "this is an outline record" in desc.lower():
        return OUTLINE
    if "format deprecated" in desc.lower():
        return DEPRECATED
    if "puid deprecated" in desc.lower():
        return DEPRECATED
    if "puid is now deprecated" in desc.lower():
        return DEPRECATED
    if "deprecated in favour" in desc.lower():
        return DEPRECATED
    if "this format has been deprecated" in desc.lower():
        return DEPRECATED
    if "this puid has been deprecated" in desc.lower():
        return DEPRECATED
    return COMPLETE


def process_name_version(name: str, version: str) -> str:
    """Process PRONOM format names and irregularities."""
    if version == "" or version is None:
        return name.strip()
    return f"{name.strip()} {version.strip()}"


def summarize_xml(pronom_xml: list[Path]):
    """Summarize the fmt XML record.

    If the record cannot be parsed correctly for any reason a
    PRONOMException is raised.
    """
    try:
        tree = etree.parse(pronom_xml)
    except ParseError as err:
        raise PRONOMException(f"cannot parse xml: {pronom_xml}") from err
    root = tree.getroot()
    name = root.find(
        "pro:report_format_detail/pro:FileFormat/pro:FormatName", NAMESPACES
    )
    version = root.find(
        "pro:report_format_detail/pro:FileFormat/pro:FormatVersion", NAMESPACES
    )
    desc = root.find(
        "pro:report_format_detail/pro:FileFormat/pro:FormatDescription", NAMESPACES
    )
    identifiers = root.findall(
        "pro:report_format_detail/pro:FileFormat/pro:FileFormatIdentifier", NAMESPACES
    )
    sig = root.find(
        "pro:report_format_detail/pro:FileFormat/pro:InternalSignature/pro:ByteSequence/pro:ByteSequenceValue",
        NAMESPACES,
    )
    puid = get_puid(identifiers)
    res = {}
    try:
        res["name"] = f"{process_name_version(name.text, version.text)}".strip()
        res["description"] = process_desc(desc.text)
        res["signature"] = sig is not None
        res["identifier"] = puid
    except AttributeError as err:
        raise PRONOMException(f"cannot process {pronom_xml}") from err
    return res


async def parse_pronom(pronom_export: str, container_signature: str) -> list[dict]:
    """Parse PRONOM's records and container signature file and return a
    list of information we want to understand better sorted by file
    format name in alphabetical order.
    """
    puid_path = Path(pronom_export)
    xml = []
    for item in puid_path.glob("**/*"):
        if not item.is_file():
            continue
        xml.append(Path(item.resolve()))
    pronom_summary = []
    with multiprocessing.Pool() as pool:
        pronom_summary = pool.map(summarize_xml, xml)
    container_summary = summarize_container_xml(container_signature)
    for item in pronom_summary:
        if item.get("identifier") not in container_summary:
            continue
        item["container signauture"] = True
    return sorted(pronom_summary, key=lambda item: item["name"])


def main():
    """Primary entry point for this script."""

    rel = pronom_tools.check_existing()
    container_name = pronom_tools.download_container(rel=rel)
    pronom_summary = asyncio.run(
        parse_pronom(
            pronom_export="pronom-export",
            container_signature=container_name,
        )
    )
    print(json.dumps(pronom_summary, indent=2))


if __name__ == "__main__":
    main()
