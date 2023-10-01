"""Test PRONOM summary code."""

from typing import Final

import pytest

from src.pronom_summary.pronom_summary import (
    PRONOMException,
    summarize_container_xml,
    summarize_xml,
)

XML_1: Final[
    str
] = """<?xml version="1.0" encoding="utf-8"?>
<PRONOM-Report xmlns="http://pronom.nationalarchives.gov.uk">
  <report_format_detail>
    <FileFormat>
      <FormatName>Test 1</FormatName>
      <FormatVersion>Test 1</FormatVersion>
      <FormatDescription>Broadcast WAVE is a chunk-based audio format developed by the European Broadcasting Union, and based on the Microsoft WAVE format, which is in turn based on the generic Resource Interchange File Format (RIFF) specification developed by Microsoft and IBM. Structurally, a BWAVE file is composed of a number of chunks, each comprising a four character code chunk identifier, the chunk size, and the chunk data. It comprises a RIFF header with a WAVE data type identifier, followed by a series of chunks. Every file must include a Broadcast Audio Extension chunk, containing metadata required for exchange of information between broadcasters, a Format chunk, which describes the format of the audio data, and a Data chunk, containing the audio data itself. BWAVE files which contain MPEG-encoded audio data must also include a Fact chunk, containing file-dependent information about the audio data, and an MPEG Audio Extension chunk, containing extra information required to describe the MPEG encoding.  A BWAVE identified as generic by DROID likely uses an encoding format unknown to PRONOM, or perhaps a structural difference, and users are encouraged to let the PRONOM team know should this occur.</FormatDescription>
      <FileFormatIdentifier>
        <Identifier>audio/x-wav</Identifier>
        <IdentifierType>MIME</IdentifierType>
      </FileFormatIdentifier>
      <FileFormatIdentifier>
        <Identifier>fmt/1</Identifier>
        <IdentifierType>PUID</IdentifierType>
      </FileFormatIdentifier>
      <InternalSignature>
        <SignatureID>1032</SignatureID>
        <SignatureName>BWAVE Generic 0</SignatureName>
        <SignatureNote>RIFF header, WAVE ID, BEXT chunk (Version=0)</SignatureNote>
        <ByteSequence>
          <ByteSequenceID>1273</ByteSequenceID>
          <PositionType>Absolute from BOF</PositionType>
          <Offset>0</Offset>
          <MaxOffset>0</MaxOffset>
          <IndirectOffsetLocation>
          </IndirectOffsetLocation>
          <IndirectOffsetLength>
          </IndirectOffsetLength>
          <Endianness>
          </Endianness>
          <ByteSequenceValue>52494646{4}57415645*62657874{350}0000</ByteSequenceValue>
        </ByteSequence>
      </InternalSignature>
    </FileFormat>
    <SearchCriteria>Criteria</SearchCriteria>
  </report_format_detail>
</PRONOM-Report>
"""

XML_2: Final[
    str
] = """<release_notes>
</release_notes>
"""

XML_3: Final[
    str
] = """<?xml version="1.0" encoding="utf-8"?>
<PRONOM-Report xmlns="http://pronom.nationalarchives.gov.uk">
  <report_format_detail>
    <FileFormat>
      <FormatName>Test 3</FormatName>
      <FormatVersion>Test 3</FormatVersion>
      <FormatDescription>This is an outline record only</FormatDescription>
      <FileFormatIdentifier>
        <Identifier>audio/x-wav</Identifier>
        <IdentifierType>MIME</IdentifierType>
      </FileFormatIdentifier>
      <FileFormatIdentifier>
        <Identifier>fmt/1</Identifier>
        <IdentifierType>PUID</IdentifierType>
      </FileFormatIdentifier>
    </FileFormat>
    <SearchCriteria>Criteria</SearchCriteria>
  </report_format_detail>
</PRONOM-Report>
"""

NOT_XML_1: Final[str] = "NO DATA HERE"

RES_1 = {
    "name": "Test 1 Test 1",
    "description": "complete",
    "signature": True,
    "identifier": "fmt/1",
}
RES_3 = {
    "name": "Test 3 Test 3",
    "description": "outline",
    "signature": False,
    "identifier": "fmt/1",
}


@pytest.mark.parametrize(
    "xml, expected, exception",
    [
        (XML_1, RES_1, False),
        (XML_2, {}, True),
        (NOT_XML_1, {}, True),
        (XML_3, RES_3, False),
    ],
)
def test_summarize(xml, expected, exception, tmp_path):
    """Test the primary summarize function of the script."""
    xml_path = tmp_path / "tmp.xml"
    xml_path.write_text(xml.strip())
    if exception:
        with pytest.raises(PRONOMException):
            res = summarize_xml(xml_path)
        return
    res = summarize_xml(xml_path)
    print(res)
    assert res == expected


CONTAINER_SIGNATURE: Final[
    str
] = """
<?xml version="1.0" encoding="UTF-8"?>

<ContainerSignatureMapping schemaVersion="1.0" signatureVersion="35">

  <ContainerSignatures>
    <ContainerSignature Id="1000" ContainerType="OLE2">
      <Description>Microsoft Word 6.0/95 OLE2</Description>
      <Files>
        <File>
          <Path>WordDocument</Path>
        </File>
        <File>
          <Path>CompObj</Path>
          <BinarySignatures>
            <InternalSignatureCollection>
              <InternalSignature ID="306">
                <ByteSequence Reference="BOFoffset">
                  <SubSequence Position="1" SubSeqMinOffset="40"
                    SubSeqMaxOffset="1024">
                    <Sequence>10 00 00 00 'Word.Document.' ['6'-'7']
                      00</Sequence>
                  </SubSequence>
                </ByteSequence>
              </InternalSignature>
            </InternalSignatureCollection>
          </BinarySignatures>
        </File>
      </Files>
    </ContainerSignature>
  </ContainerSignatures>


  <FileFormatMappings>
    <!--  Microsoft Word 6.0/95 (OLE2)-->
    <FileFormatMapping signatureId="1000" Puid="fmt/39"/>
    <!--  Microsoft Word 97 (OLE2)-->
    <FileFormatMapping signatureId="1020" Puid="fmt/40"/>
    <!-- Microsoft Word OOXML (ZIP)-->
    <FileFormatMapping signatureId="1030" Puid="fmt/412"/>
    <!-- Microsoft Word OOXML little endian (ZIP)-->
    <FileFormatMapping signatureId="1040" Puid="fmt/412"/>
    <!-- Microsoft Word OOXML big endian (ZIP)-->
    <FileFormatMapping signatureId="1050" Puid="x-fmt/412"/>
  </FileFormatMappings>

  <TriggerPuids>
    <TriggerPuid ContainerType="OLE2" Puid="fmt/111"/>
    <TriggerPuid ContainerType="ZIP" Puid="fmt/189"/>
    <TriggerPuid ContainerType="ZIP" Puid="x-fmt/263"/>
  </TriggerPuids>

</ContainerSignatureMapping>
"""


def test_container_match(tmp_path):
    """Test that the container matching to standard signatures
    works."""
    xml_path = tmp_path / "tmp.xml"
    xml_path.write_text(CONTAINER_SIGNATURE.strip())
    res = summarize_container_xml(xml_path)
    assert res == [
        "fmt/39",
        "fmt/40",
        "fmt/412",
        "fmt/412",
        "x-fmt/412",
    ]
