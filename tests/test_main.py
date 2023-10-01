"""Placeholder tests."""

from src.pronom_tools.pronom_tools import (
    parse_http_date,
    parse_release_date,
    parse_release_xml,
    parse_signature_file_string,
)

# pylint: disable=C0302

RELEASE_XML = """
<?xml version="1.0" encoding="utf-8"?>
<?xml-stylesheet type="text/xsl" href="release-note.xsl"?>
<release_notes>
<release_note>
   <release_date>22nd August 2023</release_date>
   <signature_filename>DROID_SignatureFile_V114.xml</signature_filename>
   <release_outline name="New Records">
      <format>
         <puid type="fmt">1862</puid>
         <name>Adobe Illustrator CC Artwork 17-23</name>
         <summary>Full entry added. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1863</puid>
         <name>Adobe Illustrator CC 2020 Artwork 24.0-24.1</name>
         <summary>Full entry added. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1864</puid>
         <name>Adobe Illustrator CC 2020 Artwork 24.2+</name>
         <summary>Full entry added. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1865</puid>
         <name>SWiSH Movie File</name>
         <summary>Full entry added. Submitted by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">1866</puid>
         <name>Microsoft Powerpoint for Macintosh v.2</name>
         <summary>Full entry added. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1867</puid>
         <name>Microsoft Powerpoint for Macintosh v.3</name>
         <summary>Full entry added. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1868</puid>
         <name>Leapfrog Geo 3D Scene Format</name>
         <summary>Full entry added. Submitted by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">1869</puid>
         <name>SPSS PC File Format</name>
         <summary>Full entry added. Submitted by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">1870</puid>
         <name>Yamaha PSR Disk Manager File</name>
         <summary>Full entry added. Submitted by R. Guedj, Bibliothèque Cantonale Universitaire de Fribourg.</summary>
      </format>
      <format>
         <puid type="fmt">1871</puid>
         <name>Common Interface File</name>
         <summary>Full entry added. Submitted by Transport for London.</summary>
      </format>
      <format>
         <puid type="fmt">1872</puid>
         <name>Guitar Pro File 1</name>
         <summary>Full entry added. Submitted by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1873</puid>
         <name>Guitar Pro File 2-5</name>
         <summary>Full entry added. Submitted by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1874</puid>
         <name>Esko ArtPro File</name>
         <summary>Full entry added. Submitted by The Church of Jesus Christ of Latter-day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1875</puid>
         <name>Maptech BSB Documentation File</name>
         <summary>Full entry added. Submitted by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1876</puid>
         <name>HMM Packfile</name>
         <summary>Full entry added. Submitted by Ross Spencer, Ravensburger AG.</summary>
      </format>
      <format>
         <puid type="fmt">1877</puid>
         <name>GST Art File (1)</name>
         <summary>Full entry added. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1878</puid>
         <name>GST Art File (2)</name>
         <summary>Full entry added. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1879</puid>
         <name>vCard 2.1</name>
         <summary>Full entry added. Submitted by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">1880</puid>
         <name>vCard 3</name>
         <summary>Full entry added. Submitted by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">1881</puid>
         <name>vCard 4</name>
         <summary>Full entry added. Submitted by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">1882</puid>
         <name>OPML File 1.*</name>
         <summary>Full entry added. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="fmt">1883</puid>
         <name>OPML File 2</name>
         <summary>Full entry added. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="fmt">1884</puid>
         <name>Encapsulated PostScript File Format 2.1</name>
         <summary>Full entry added. Submitted by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">1885</puid>
         <name>CloudCompare Entity File</name>
         <summary>Full entry added. Submitted by National Library of New Zealand.</summary>
      </format>
      <format>
         <puid type="fmt">1886</puid>
         <name>Resource Interleaved File Format (RIFF)</name>
         <summary>Full entry added. Submitted by New York Public Libraries.</summary>
      </format>
      <format>
         <puid type="fmt">1887</puid>
         <name>Common Instrument File (CIF) 1</name>
         <summary>Full entry added. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1888</puid>
         <name>Common Instrument File (CIF) 2</name>
         <summary>Full entry added. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1889</puid>
         <name>Open Access III Document</name>
         <summary>Full entry added. Submitted by National Library of New Zealand.</summary>
      </format>
      <format>
         <puid type="fmt">1890</puid>
         <name>Memory Stick Voice File (MSV) ADPCM Codec</name>
         <summary>Full entry added. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1891</puid>
         <name>Digital Voice File (DVF) TRC Codec</name>
         <summary>Full entry added. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1892</puid>
         <name>Memory Stick Voice File (MSV)/Digital Voice File (DVF) LPEC Codec</name>
         <summary>Full entry added. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1893</puid>
         <name>Microsoft Agent File</name>
         <summary>Full entry added. Submitted by New York Public Libraries.</summary>
      </format>
      <format>
         <puid type="fmt">1894</puid>
         <name>RagTime Document File 2-3</name>
         <summary>Full entry added. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1895</puid>
         <name>RagTime Document File 4-6</name>
         <summary>Full entry added. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1896</puid>
         <name>Nokia Picture Message</name>
         <summary>Full entry added. Submitted by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1897</puid>
         <name>Ptex File Format</name>
         <summary>Full entry added. Submitted by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1898</puid>
         <name>Perfect ZX Tape (PZX) Image Format</name>
         <summary>Full entry added. Submitted by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1899</puid>
         <name>RIS Citation</name>
         <summary>Full entry added. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1900</puid>
         <name>Mass Spectrometry Markup Language</name>
         <summary>Full entry added. Submitted by Brigham Young University.</summary>
      </format>
   </release_outline>
   <release_outline name="Updated Records">
      <format>
         <puid type="fmt">5</puid>
         <name>Audio/Video Interleaved Format</name>
         <summary>Signature simplified to increase identification tool processing time. Added priority over fmt/1886. Submitted by Preservica and New York Public Libraries.</summary>
      </format>
      <format>
         <puid type="fmt">6</puid>
         <name>Waveform Audio</name>
         <summary>Added priority over fmt/1886. Submitted by New York Public Libraries and Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">41</puid>
         <name>Raw JPEG Stream</name>
         <summary>Offset modified for the EOF signature as null value causing max-offset to be ignored. Submitted by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">122</puid>
         <name>Encapsulated PostScript File Format 1.2</name>
         <summary>Added description of magic bytes. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="fmt">123</puid>
         <name>Encapsulated PostScript File Format 2.0</name>
         <summary>Added description of magic bytes. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="fmt">124</puid>
         <name>Encapsulated PostScript File Format 3</name>
         <summary>Added description of magic bytes and specification. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="fmt">163</puid>
         <name>Microsoft Works Word Processor 1-3 for DOS and 2 for Windows</name>
         <summary>Updated description to provide entry and added links to documentation. Signature updated with either or bytes. Max-offset of 0 bytes added for BOF signature. Submitted by Zeticon.</summary>
      </format>
      <format>
         <puid type="fmt">179</puid>
         <name>Microsoft PowerPoint for Macintosh v.4.0</name>
         <summary>Added description and MIME type. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="fmt">181</puid>
         <name>Microsoft PowerPoint for Macintosh 2001</name>
         <summary>Added description and MIME type. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="fmt">199</puid>
         <name>MPEG-4 Media File</name>
         <summary>Added priority over fmt/1616. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="fmt">385</puid>
         <name>Microsoft Windows Cursor</name>
         <summary>Offsets removed from variable byte sequence and updated description. Submitted by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">386</puid>
         <name>Microsoft Animated Cursor Format</name>
         <summary>Added priority over fmt/1886. Submitted by New York Public Libraries and Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">389</puid>
         <name>Log ASCII Standard 1.2</name>
         <summary>Offset added to signature to accomodate header. Submitted by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">395</puid>
         <name>vCard</name>
         <summary>Added vcard extension, updated description. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="fmt">427</puid>
         <name>CorelDraw Drawing 12.0</name>
         <summary>Added priority over fmt/1886. Submitted by New York Public Libraries and Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">428</puid>
         <name>CorelDraw Drawing X3</name>
         <summary>Added priority over fmt/1886. Submitted by New York Public Libraries and Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">431</puid>
         <name>Corel R.A.V.E. 2</name>
         <summary>Added priority over fmt/1886 and updated description. Submitted by New York Public Libraries and Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">432</puid>
         <name>Corel R.A.V.E. 3</name>
         <summary>Added priority over fmt/1886 and updated description. Submitted by New York Public Libraries and Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">464</puid>
         <name>CorelDraw Drawing 5.0</name>
         <summary>Added priority over fmt/1886. Submitted by New York Public Libraries and Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">465</puid>
         <name>CorelDraw Drawing 4.0</name>
         <summary>Added priority over fmt/1886. Submitted by New York Public Libraries and Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">468</puid>
         <name>ISO 9660 Disk Image File</name>
         <summary>Max-offset modified for BOF signature to allow for more exact signature identification. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="fmt">558</puid>
         <name>Adobe Illustrator 9.0</name>
         <summary>Updated signature and links. Added WikiQID and reference to submission. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">559</puid>
         <name>Adobe Illustrator 10.0</name>
         <summary>Updated signature, links and reference to submission. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">560</puid>
         <name>Adobe Illustrator 11.0</name>
         <summary>Updated signature, links and reference to submission. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">561</puid>
         <name>Adobe Illustrator 12.0</name>
         <summary>Updated signature, links and reference to submission. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">562</puid>
         <name>Adobe Illustrator 13.0</name>
         <summary>Updated signature, links and reference to submission. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">563</puid>
         <name>Adobe Illustrator 14.0</name>
         <summary>Updated signature, links and reference to submission. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">564</puid>
         <name>Adobe Illustrator 15.0</name>
         <summary>Updated signature, links and reference to submission. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">565</puid>
         <name>Adobe Illustrator 16.0</name>
         <summary>Updated signature, links and reference to submission. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">566</puid>
         <name>WebP Lossy</name>
         <summary>Added priority over fmt/1886. Submitted by New York Public Libraries and Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">567</puid>
         <name>WebP Lossless</name>
         <summary>Added priority over fmt/1886. Submitted by New York Public Libraries and Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">568</puid>
         <name>WebP Extended</name>
         <summary>Added priority over fmt/1886. Submitted by New York Public Libraries and Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">624</puid>
         <name>RIFF Palette Format</name>
         <summary>Added priority over fmt/1886. Submitted by New York Public Libraries and Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">649</puid>
         <name>MPEG-2 Elementary Stream</name>
         <summary>Added priority over fmt/640 MPEG-1 Elementary Stream. Submitted by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">657</puid>
         <name>Open XML Paper Specification</name>
         <summary>Added extension oxps. Submitted by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">819</puid>
         <name>CD-ROM/XA (eXtended Architecture)</name>
         <summary>Added priority over fmt/1886. Submitted by New York Public Libraries and Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">882</puid>
         <name>Wordstar 2000</name>
         <summary>Changed offset from 128 to 130. Submitted by National Library of New Zealand.</summary>
      </format>
      <format>
         <puid type="fmt">923</puid>
         <name>Microsoft xWMA</name>
         <summary>Added priority over fmt/1886. Submitted by New York Public Libraries and Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">955</puid>
         <name>Downloadable Sounds Audio</name>
         <summary>Added priority over fmt/1886. Submitted by New York Public Libraries and Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">956</puid>
         <name>RIFF-based MIDI</name>
         <summary>Added priority over fmt/1886. Submitted by New York Public Libraries and Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">957</puid>
         <name>DirectMusic Segment File Format</name>
         <summary>Added priority over fmt/1886. Submitted by New York Public Libraries and Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">958</puid>
         <name>DirectMusic Style File Format</name>
         <summary>Added priority over fmt/1886. Submitted by New York Public Libraries and Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">962</puid>
         <name>QCP Audio File Format</name>
         <summary>Added priority over fmt/1886. Submitted by New York Public Libraries and Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1150</puid>
         <name>4X Movie File</name>
         <summary>Added priority over fmt/1886. Submitted by New York Public Libraries and Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1155</puid>
         <name>Lightwright Show File (5)</name>
         <summary>Offset modified for the EOF signature as null value causing max-offset to be ignored. Submitted by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1210</puid>
         <name>Wavefront OBJ File</name>
         <summary>Modified BOF signature to increase two of the byte ranges. Submitted by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1556</puid>
         <name>Lightwright Show File (6)</name>
         <summary>Offset modified for the EOF signature as null value causing max-offset to be ignored. Submitted by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1739</puid>
         <name>UDF-ISO 9660 Bridge Disc</name>
         <summary>Max-offset modified for both BOF signatures to allow for more exact signature identification. Internally researched. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="fmt">1776</puid>
         <name>Extensible Markup Language 1.1</name>
         <summary>Relationship with fmt/101 added and signature tightened to prevent clashes with fmt/92. Submitted by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1778</puid>
         <name>Gunpaint Image File</name>
         <summary>Adjusted signature to include 'GUNPAINT' at an offset of 1002 from BOF. Submitted by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1796</puid>
         <name>Wireless Markup Language (WML) Document</name>
         <summary>Offset and signature modified for the EOF byte sequence to remove floating curly brackets from the signature for consistency. Submitted by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1850</puid>
         <name>WordPerfect Macro File</name>
         <summary>Priority added over x-fmt/393 (WordPerfect for MS-DOS Document 5.0). Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="x-fmt">29</puid>
         <name>CorelDraw Drawing 6.0</name>
         <summary>Added priority over fmt/1886. Submitted by New York Public Libraries and Preservica.</summary>
      </format>
      <format>
         <puid type="x-fmt">33</puid>
         <name>Corel R.A.V.E. 1</name>
         <summary>Added priority over fmt/1886. Submitted by New York Public Libraries and Preservica.</summary>
      </format>
      <format>
         <puid type="x-fmt">34</puid>
         <name>Corel Presentation Exchange File 5.0</name>
         <summary>Added priority over fmt/1886. Submitted by New York Public Libraries and Preservica.</summary>
      </format>
      <format>
         <puid type="x-fmt">35</puid>
         <name>Corel Presentation Exchange File 6 and Later</name>
         <summary>Added priority over fmt/1886. Submitted by New York Public Libraries and Preservica.</summary>
      </format>
      <format>
         <puid type="x-fmt">222</puid>
         <name>CD Audio</name>
         <summary>Added priority over fmt/1886. Submitted by New York Public Libraries and Preservica.</summary>
      </format>
      <format>
         <puid type="x-fmt">291</puid>
         <name>CorelDraw Drawing 7.0</name>
         <summary>Added priority over fmt/1886. Submitted by New York Public Libraries and Preservica.</summary>
      </format>
      <format>
         <puid type="x-fmt">292</puid>
         <name>CorelDraw Drawing 8.0</name>
         <summary>Added priority over fmt/1886. Submitted by New York Public Libraries and Preservica.</summary>
      </format>
      <format>
         <puid type="x-fmt">374</puid>
         <name>CorelDraw Drawing 9.0</name>
         <summary>Added priority over fmt/1886. Submitted by New York Public Libraries and Preservica.</summary>
      </format>
      <format>
         <puid type="x-fmt">375</puid>
         <name>CorelDraw Drawing 10.0</name>
         <summary>Added priority over fmt/1886. Submitted by New York Public Libraries and Preservica.</summary>
      </format>
      <format>
         <puid type="x-fmt">378</puid>
         <name>CorelDraw Drawing 11.0</name>
         <summary>Added priority over fmt/1886. Submitted by New York Public Libraries and Preservica.</summary>
      </format>
      <format>
         <puid type="x-fmt">379</puid>
         <name>CorelDraw Drawing 3.0</name>
         <summary>Added priority over fmt/1886. Submitted by New York Public Libraries and Preservica.</summary>
      </format>
   </release_outline>
   <release_outline name="New Signatures">
      <format>
         <puid type="fmt">1862</puid>
         <name>Adobe Illustrator CC Artwork 17-23</name>
         <summary>Signature researched and samples provided by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1863</puid>
         <name>Adobe Illustrator CC 2020 Artwork 24.0-24.1</name>
         <summary>Signature researched and samples provided by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1864</puid>
         <name>Adobe Illustrator CC 2020 Artwork 24.2+</name>
         <summary>Signature researched and samples provided by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1865</puid>
         <name>SWiSH Movie File</name>
         <summary>Signature researched and samples provided by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">1866</puid>
         <name>Microsoft Powerpoint for Macintosh v.2</name>
         <summary>Signature researched and samples provided by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1867</puid>
         <name>Microsoft Powerpoint for Macintosh v.3</name>
         <summary>Signature researched and samples provided by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1868</puid>
         <name>Leapfrog Geo 3D Scene Format</name>
         <summary>Signature researched and samples provided by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">1869</puid>
         <name>SPSS PC File Format</name>
         <summary>Signature researched and samples provided by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">1870</puid>
         <name>Yamaha PSR Disk Manager File</name>
         <summary>Signature researched and samples provided by R. Guedj, Bibliothèque Cantonale Universitaire de Fribourg.</summary>
      </format>
      <format>
         <puid type="fmt">1871</puid>
         <name>Common Interface File</name>
         <summary>Signature researched and samples provided by Transport for London.</summary>
      </format>
      <format>
         <puid type="fmt">1872</puid>
         <name>Guitar Pro File 1</name>
         <summary>Signature researched and samples provided by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1873</puid>
         <name>Guitar Pro File 2-5</name>
         <summary>Signature researched and samples provided by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1874</puid>
         <name>Esko ArtPro File</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1875</puid>
         <name>Maptech BSB Documentation File</name>
         <summary>Signature researched and samples provided by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1876</puid>
         <name>HMM Packfile</name>
         <summary>Signature researched and samples provided by Ross Spencer, Ravensburger AG.</summary>
      </format>
      <format>
         <puid type="fmt">1877</puid>
         <name>GST Art File (1)</name>
         <summary>Signature researched and samples provided by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1878</puid>
         <name>GST Art File (2)</name>
         <summary>Signature researched and samples provided by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1879</puid>
         <name>vCard 2.1</name>
         <summary>Signature researched and samples provided by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">1880</puid>
         <name>vCard 3</name>
         <summary>Signature researched and samples provided by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">1881</puid>
         <name>vCard 4</name>
         <summary>Signature researched and samples provided by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">1882</puid>
         <name>OPML File 1.*</name>
         <summary>Signature researched and samples provided by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="fmt">1883</puid>
         <name>OPML File 2</name>
         <summary>Signature researched and samples provided by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="fmt">1884</puid>
         <name>Encapsulated PostScript File Format 2.1</name>
         <summary>Signature researched and samples provided by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">1885</puid>
         <name>CloudCompare Entity File</name>
         <summary>Signature researched and samples provided by National Library of New Zealand.</summary>
      </format>
      <format>
         <puid type="fmt">1886</puid>
         <name>Resource Interleaved File Format (RIFF)</name>
         <summary>Signature researched and samples provided by New York Public Libraries.</summary>
      </format>
      <format>
         <puid type="fmt">1887</puid>
         <name>Common Instrument File (CIF) 1</name>
         <summary>Signature researched and samples provided by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1888</puid>
         <name>Common Instrument File (CIF) 2</name>
         <summary>Signature researched and samples provided by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1889</puid>
         <name>Open Access III Document</name>
         <summary>Signature researched and samples provided by National Library of New Zealand.</summary>
      </format>
      <format>
         <puid type="fmt">1890</puid>
         <name>Memory Stick Voice File (MSV) ADPCM Codec</name>
         <summary>Signature researched and samples provided by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1891</puid>
         <name>Digital Voice File (DVF) TRC Codec</name>
         <summary>Signature researched and samples provided by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1892</puid>
         <name>Memory Stick Voice File (MSV)/Digital Voice File (DVF) LPEC Codec</name>
         <summary>Signature researched and samples provided by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1893</puid>
         <name>Microsoft Agent File</name>
         <summary>Signature researched and samples provided by New York Public Libraries.</summary>
      </format>
      <format>
         <puid type="fmt">1894</puid>
         <name>RagTime Document File 2-3</name>
         <summary>Signature researched and samples provided by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1895</puid>
         <name>RagTime Document File 4-6</name>
         <summary>Signature researched and samples provided by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1896</puid>
         <name>Nokia Picture Message</name>
         <summary>Signature researched and samples provided by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1897</puid>
         <name>Ptex File Format</name>
         <summary>Signature researched and samples provided by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1898</puid>
         <name>Perfect ZX Tape (PZX) Image Format</name>
         <summary>Signature researched and samples provided by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1899</puid>
         <name>RIS Citation</name>
         <summary>Signature researched and samples provided by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1900</puid>
         <name>Mass Spectrometry Markup Language</name>
         <summary>Signature researched and samples provided by Brigham Young University.</summary>
      </format>
   </release_outline>
</release_note>
<release_note>
   <release_date>10th May 2023</release_date>
   <signature_filename>DROID_SignatureFile_V112.xml</signature_filename>
   <release_outline name="New Records">
      <format>
         <puid type="fmt">1845</puid>
         <name>Final Draft Document v.8</name>
         <summary>Full entry added. Submitted by Stadtarchiv Hof (Municipal Archives of Hof, Free State of Bavaria, Germany).</summary>
      </format>
      <format>
         <puid type="fmt">1846</puid>
         <name>Fountain Markup Language File</name>
         <summary>Extension-only entry added. Submitted by Stadtarchiv Hof (Municipal Archives of Hof, Free State of Bavaria, Germany).</summary>
      </format>
      <format>
         <puid type="fmt">1847</puid>
         <name>Esri ArcMap Label File</name>
         <summary>Extension-only entry added. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1848</puid>
         <name>Trelby Document File</name>
         <summary>Full entry added. Submitted by Stadtarchiv Hof (Municipal Archives of Hof, Free State of Bavaria, Germany).</summary>
      </format>
      <format>
         <puid type="fmt">1849</puid>
         <name>General Purpose RAW (GoPro GPR)</name>
         <summary>Full entry added. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1850</puid>
         <name>WordPerfect Macro File</name>
         <summary>Full entry added. Submitted by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">1851</puid>
         <name>DAV Video Format</name>
         <summary>Full entry added. Submitted by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1852</puid>
         <name>Camtasia Recording File</name>
         <summary>Full entry added. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1853</puid>
         <name>Camtasia Studio Project</name>
         <summary>Full entry added. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1854</puid>
         <name>Open Media Framework Interchange 1.0</name>
         <summary>Full entry added. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1855</puid>
         <name>Open Media Framework Interchange 2.0</name>
         <summary>Full entry added. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1856</puid>
         <name>Enhanced Image Package</name>
         <summary>Full entry added. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1857</puid>
         <name>Capture One Session File</name>
         <summary>Full entry added. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1858</puid>
         <name>Microsoft Excel Workspace File 5/95</name>
         <summary>Full entry added. Submitted by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">1859</puid>
         <name>Adobe Air 2.5</name>
         <summary>Extension-only entry added. Submitted by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">1860</puid>
         <name>dBASE Report Form Definition File IV</name>
         <summary>Full entry added. Submitted by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">1861</puid>
         <name>Quicken 3 Database File</name>
         <summary>Full entry added. Submitted by The National Library of Australia.</summary>
      </format>
   </release_outline>
   <release_outline name="Updated Records">
      <format>
         <puid type="fmt">175</puid>
         <name>Microsoft Excel for Macintosh 2001</name>
         <summary>PUID deprecated. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">176</puid>
         <name>Microsoft Excel for Macintosh 2002</name>
         <summary>PUID deprecated. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">177</puid>
         <name>Microsoft Excel for Macintosh 2004</name>
         <summary>PUID deprecated. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">205</puid>
         <name>Synchronized Multimedia Integration Language</name>
         <summary>Updated signature. Submitted by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">649</puid>
         <name>MPEG-1 Elementary Stream</name>
         <summary>Updated signature by broadening byte range. Submitted by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">696</puid>
         <name>Sibelius</name>
         <summary>Updated signature description. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="fmt">803</puid>
         <name>Encase Image File/Expert Witness Compression File</name>
         <summary>Updated name, added priority over ISO 9660 Disk Image File. Submitted by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">938</puid>
         <name>Python Source Code File</name>
         <summary>Updated name and description and added a link to the official documentation. Submitted by Stadtarchiv Hof (Municipal Archives of Hof, Free State of Bavaria, Germany).</summary>
      </format>
      <format>
         <puid type="fmt">964</puid>
         <name>Final Draft Document 5-7</name>
         <summary>Added relationship and developer. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="fmt">1149</puid>
         <name>Markdown</name>
         <summary>Added extension .markdown and reference links. Submitted by Stadtarchiv Hof (Municipal Archives of Hof, Free State of Bavaria, Germany).</summary>
      </format>
      <format>
         <puid type="fmt">1213</puid>
         <name>Zoner Callisto Metafile 2</name>
         <summary>Extension changed from .f to .zmf. Submitted by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1218</puid>
         <name>SubRip Subtitle File</name>
         <summary>Updated description and added reference links. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="fmt">1649</puid>
         <name>AGS 4 Data Format 4.0 4.1</name>
         <summary>Broadened main body of signature and added BOF sequence. Submitted by Preservica and Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="fmt">1805</puid>
         <name>Microsoft Access Database File 1.0</name>
         <summary>Updated Wikidata QID. Submitted by Yale University Library.</summary>
      </format>
      <format>
         <puid type="fmt">1806</puid>
         <name>Microsoft Access Database File 1.1</name>
         <summary>Updated Wikidata QID. Submitted by Yale University Library.</summary>
      </format>
      <format>
         <puid type="fmt">1807</puid>
         <name>Microsoft Access Encrypted Database File 1.0</name>
         <summary>Updated Wikidata QID. Submitted by Yale University Library.</summary>
      </format>
      <format>
         <puid type="fmt">1808</puid>
         <name>Microsoft Access Encrypted Database File 1.1</name>
         <summary>Updated Wikidata QID. Submitted by Yale University Library.</summary>
      </format>
      <format>
         <puid type="fmt">1809</puid>
         <name>Microsoft Access Encrypted Database File 2.0</name>
         <summary>Updated Wikidata QID. Submitted by Yale University Library.</summary>
      </format>
      <format>
         <puid type="fmt">1813</puid>
         <name>xdomea 3.0.0</name>
         <summary>Updated priority. Submitted by Preservica.</summary>
      </format>
      <format>
         <puid type="x-fmt">8</puid>
         <name>dBASE Database II</name>
         <summary>Added developer. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="x-fmt">9</puid>
         <name>dBASE Database III</name>
         <summary>Added developer. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="x-fmt">10</puid>
         <name>dBASE Database IV</name>
         <summary>Added developer. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="x-fmt">13</puid>
         <name>Tab-separated Values</name>
         <summary>Added extension .tab, added reference links, identifiers for LoC and Wikidata QID. Submitted by Brigham Young University and Preservica.</summary>
      </format>
      <format>
         <puid type="x-fmt">66</puid>
         <name>Microsoft Access Database File 2.0</name>
         <summary>Updated Wikidata QID. Submitted by National Library of the Netherlands.</summary>
      </format>
      <format>
         <puid type="x-fmt">128</puid>
         <name>Microsoft Excel Workspace File</name>
         <summary>Added description. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="x-fmt">238</puid>
         <name>Microsoft Access Database File 95</name>
         <summary>Updated Wikidata QID. Submitted by National Library of the Netherlands.</summary>
      </format>
      <format>
         <puid type="x-fmt">239</puid>
         <name>Microsoft Access Database File 97</name>
         <summary>Updated Wikidata QID. Submitted by National Library of the Netherlands.</summary>
      </format>
      <format>
         <puid type="x-fmt">240</puid>
         <name>Microsoft Access Database File 2000</name>
         <summary>Updated Wikidata QID. Submitted by National Library of the Netherlands.</summary>
      </format>
      <format>
         <puid type="x-fmt">241</puid>
         <name>Microsoft Access Database File 2002</name>
         <summary>Updated Wikidata QID. Submitted by National Library of the Netherlands.</summary>
      </format>
      <format>
         <puid type="x-fmt">271</puid>
         <name>dBASE Database III+</name>
         <summary>Added developer. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="x-fmt">272</puid>
         <name>dBASE Database V</name>
         <summary>Added developer. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="x-fmt">275</puid>
         <name>Microsoft Access Database File 2007</name>
         <summary>Updated Wikidata QID, description, reference links and developer. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="x-fmt">393</puid>
         <name>WordPerfect for MS-DOS Document 5.0</name>
         <summary>Added .doc extension. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="x-fmt">394</puid>
         <name>WordPerfect for MS-DOS/Windows Document 5.1</name>
         <summary>Added .doc extension. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="x-fmt">415</puid>
         <name>Java Class File</name>
         <summary>Updated format and signature names and descriptions. Submitted by Stadtarchiv Hof (Municipal Archives of Hof, Free State of Bavaria, Germany).</summary>
      </format>
   </release_outline>
   <release_outline name="New Signatures">
      <format>
         <puid type="fmt">1845</puid>
         <name>Final Draft Document 8</name>
         <summary>Signature researched and samples provided by Stadtarchiv Hof (Municipal Archives of Hof, Free State of Bavaria, Germany).</summary>
      </format>
      <format>
         <puid type="fmt">1848</puid>
         <name>Trelby Document File</name>
         <summary>Signature researched and samples provided by Stadtarchiv Hof (Municipal Archives of Hof, Free State of Bavaria, Germany).</summary>
      </format>
      <format>
         <puid type="fmt">1849</puid>
         <name>General Purpose RAW (GoPro GPR)</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1850</puid>
         <name>WordPerfect Macro File</name>
         <summary>Signature researched and samples provided by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">1851</puid>
         <name>DAV Video Format</name>
         <summary>Signature researched and samples provided by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1852</puid>
         <name>Camtasia Recording File</name>
         <summary>Signature researched and samples provided by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1853</puid>
         <name>Camtasia Studio Project</name>
         <summary>Signature researched and samples provided by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1854</puid>
         <name>Open Media Framework Interchange 1.0</name>
         <summary>Signature researched and samples provided by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1855</puid>
         <name>Open Media Framework Interchange 2.0</name>
         <summary>Signature researched and samples provided by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1856</puid>
         <name>Enhanced Image Package</name>
         <summary>Signature researched and samples provided by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1857</puid>
         <name>Capture One Session File</name>
         <summary>Signature researched and samples provided by Brigham Young University.</summary>
      </format>
      <format>
         <puid type="fmt">1858</puid>
         <name>Microsoft Excel Workspace File</name>
         <summary>Signature researched and samples provided by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">1860</puid>
         <name>dBASE Report Form Definition File IV</name>
         <summary>Signature researched and samples provided by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">1861</puid>
         <name>Quicken 3 Database File</name>
         <summary>Signature researched and samples provided by The National Library of Australia.</summary>
      </format>
   </release_outline>
</release_note>
<release_note>
   <release_date>16th March 2023</release_date>
   <signature_filename>DROID_SignatureFile_V111.xml</signature_filename>
   <release_outline name="New Records"/>
   <release_outline name="Updated Records">
      <format>
         <puid type="fmt">1825</puid>
         <name>Audacity Project File 2.x</name>
         <summary>Priority with fmt/101 updated. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
   </release_outline>
   <release_outline name="New Signatures"/>
</release_note>
<release_note>
   <release_date>14th March 2023</release_date>
   <signature_filename>DROID_SignatureFile_V110.xml</signature_filename>
   <release_outline name="New Records">
      <format>
         <puid type="fmt">1794</puid>
         <name>JPEG 2000 Codestream</name>
         <summary>Full entry added. Submitted by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1795</puid>
         <name>Asymetrix Toolbook File 6-11.5</name>
         <summary>Full entry added. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1796</puid>
         <name>Wireless Markup Language (WML) Document</name>
         <summary>Full entry added. Submitted by Stadtarchiv Hof.</summary>
      </format>
      <format>
         <puid type="fmt">1797</puid>
         <name>SHA512 File</name>
         <summary>Extension-only entry added. Submitted by Stadtarchiv Hof.</summary>
      </format>
      <format>
         <puid type="fmt">1798</puid>
         <name>CHAT Transcription Format</name>
         <summary>Full entry added. Submitted by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1799</puid>
         <name>FLExText Interlinear XML Format</name>
         <summary>Full entry added. Submitted by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1800</puid>
         <name>Multimedia Viewer Book</name>
         <summary>Full entry added. Submitted by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1801</puid>
         <name>Praat TextGrid</name>
         <summary>Full entry added. Submitted by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1802</puid>
         <name>Transcriber AG TAG Format</name>
         <summary>Full entry added. Submitted by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1803</puid>
         <name>Transcriber TRS Format</name>
         <summary>Full entry added. Submitted by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1804</puid>
         <name>B Source Code File</name>
         <summary>Extension-only entry added. Submitted by Stadtarchiv Hof.</summary>
      </format>
      <format>
         <puid type="fmt">1805</puid>
         <name>Microsoft Access Database File 1.0</name>
         <summary>Full entry added. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1806</puid>
         <name>Microsoft Access Database File 1.1</name>
         <summary>Full entry added. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1807</puid>
         <name>Microsoft Access Encrypted Database File 1.0</name>
         <summary>Full entry added. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1808</puid>
         <name>Microsoft Access Encrypted Database File 1.1</name>
         <summary>Full entry added. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1809</puid>
         <name>Microsoft Access Encrypted Database File 2.0</name>
         <summary>Full entry added. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1810</puid>
         <name>Raw PIMA SWIR Reflectance Spectral File</name>
         <summary>Full entry added. Submitted by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">1811</puid>
         <name>Vips Image</name>
         <summary>Full entry added. Submitted by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1812</puid>
         <name>Audio Data Transport Stream</name>
         <summary>Full entry added. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1813</puid>
         <name>xdomea 3.0.0</name>
         <summary>Full entry added. Submitted by Landesarchiv Nordrhein-Westfalen.</summary>
      </format>
      <format>
         <puid type="fmt">1814</puid>
         <name>Adobe Color Book for Windows</name>
         <summary>Full entry added. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1815</puid>
         <name>Adobe Color Swatch</name>
         <summary>Extension-only entry added. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1816</puid>
         <name>Adobe Swatch Exchange</name>
         <summary>Full entry added. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1817</puid>
         <name>Direct Stream Digital Stream File</name>
         <summary>Full entry added. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1818</puid>
         <name>Direct Stream Digital Interchange File Format</name>
         <summary>Full entry added. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1819</puid>
         <name>MacCaption File 1</name>
         <summary>Full entry added. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1820</puid>
         <name>MacCaption File 2</name>
         <summary>Full entry added. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1821</puid>
         <name>MacCaption Project</name>
         <summary>Full entry added. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1822</puid>
         <name>Audacity Audio Block File</name>
         <summary>Full entry added. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1823</puid>
         <name>Audacity Project File Early</name>
         <summary>Full entry added. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1824</puid>
         <name>Audacity Project File 1.x</name>
         <summary>Full entry added. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1825</puid>
         <name>Audacity Project File 2.x</name>
         <summary>Full entry added. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1826</puid>
         <name>Audacity Project File 3.x</name>
         <summary>Full entry added. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1827</puid>
         <name>DOCX Strict OOXML Document</name>
         <summary>Full entry added. Submitted by Danish National Archives and Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1828</puid>
         <name>XLSX Strict OOXML Spreadsheet</name>
         <summary>Full entry added. Submitted by Danish National Archives and Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1829</puid>
         <name>PPTX Strict OOXML Presentation</name>
         <summary>Full entry added. Submitted by Danish National Archives and Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1830</puid>
         <name>3D Studio (DOS) 2D/3D Loft Object File</name>
         <summary>Full entry added. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1831</puid>
         <name>3D Studio (DOS) Project File</name>
         <summary>Full entry added. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1832</puid>
         <name>ArcSoft PhotoStudio File</name>
         <summary>Full entry added. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1833</puid>
         <name>ArcSoft Album and SlideShow Files for PhotoStudio and PhotoImpression</name>
         <summary>Full entry added. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1834</puid>
         <name>GoDot 4Bit Graphics Format</name>
         <summary>Full entry added. Submitted by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1835</puid>
         <name>Archiver Format</name>
         <summary>Full entry added. Submitted by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1836</puid>
         <name>Brio Query File</name>
         <summary>Full entry added. Submitted by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1837</puid>
         <name>WordPerfect Presentations</name>
         <summary>Full entry added. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1838</puid>
         <name>Leica Project File</name>
         <summary>Full entry added. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1839</puid>
         <name>Microsoft Publisher Packaged Document</name>
         <summary>Full entry added. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1840</puid>
         <name>WACZ</name>
         <summary>Full entry added. Submitted by The National Archives and Records Administration and Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1841</puid>
         <name>Digital Negative Format (DNG) 1.5</name>
         <summary>Full entry added. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1842</puid>
         <name>Digital Negative Format (DNG) 1.6</name>
         <summary>Full entry added. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1843</puid>
         <name>Human Machine Interfaces HMI File</name>
         <summary>Full entry added. Submitted by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1844</puid>
         <name>GNU Image Manipulation Program Palette File</name>
         <summary>Full entry added. Submitted by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="sfw">3</puid>
         <name>Windows NT 10.0</name>
         <summary>Windows NT 10 software information added. Submitted by Earldridge Jazzed Pineda .</summary>
      </format>
   </release_outline>
   <release_outline name="Updated Records">
      <format>
         <puid type="fmt">118</puid>
         <name>Windows Bitmap 4.0</name>
         <summary>Last pair of zeros removed from signature. Submitted by GoldFynch eDiscovery.</summary>
      </format>
      <format>
         <puid type="fmt">119</puid>
         <name>Windows Bitmap 5.0</name>
         <summary>Last pair of zeros removed from signature. Submitted by GoldFynch eDiscovery.</summary>
      </format>
      <format>
         <puid type="fmt">470</puid>
         <name>Asymetrix Toolbook File 1-5</name>
         <summary>Expanded the signature, updated description and notes. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">645</puid>
         <name>Exchangeable Image File Format (Compressed)</name>
         <summary>Version corrected from 2.2.1 to 2.21. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="fmt">899</puid>
         <name>Windows Portable Executable 32 bit</name>
         <summary>Added Portable Executable Format document, notes field updated. Submitted by Earldridge Jazzed Pineda .</summary>
      </format>
      <format>
         <puid type="fmt">900</puid>
         <name>Windows Portable Executable 64 bit</name>
         <summary>Added Portable Executable Format document, notes field updated. Submitted by Earldridge Jazzed Pineda .</summary>
      </format>
      <format>
         <puid type="fmt">1215</puid>
         <name>ERDAS Hierarchical File Architecture Format/Reduced Resolution Dataset</name>
         <summary>Name of sig and internal sig changed to Reduced Resolution Dataset, to refect the fact that this file is not just ERDAS. Submitted by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">1218</puid>
         <name>SubRip Subtitle File</name>
         <summary>Added internal signature. Submitted by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1288</puid>
         <name>IESNA LM-63 Photometric Data File</name>
         <summary>Signature modified to give an either or after initial byte sequence. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1314</puid>
         <name>GL Transmission Format (Text) 1.x</name>
         <summary>Signature changed to allow files with minor or revision version numbers to be correctly identified, file format version and signature name changed to reflect this. Submitted by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1315</puid>
         <name>GL Transmission Format (Text) 2.x</name>
         <summary>Signature changed to allow files with minor or revision version numbers to be correctly identified, file format version and signature name changed to reflect this. Submitted by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1374</puid>
         <name>xdomea 1.0</name>
         <summary>Changed xdomea from uppercase to lowercase. Submitted by Landesarchiv Nordrhein-Westfalen.</summary>
      </format>
      <format>
         <puid type="fmt">1375</puid>
         <name>xdomea 2.0.0</name>
         <summary>Changed xdomea from uppercase to lowercase. Submitted by Landesarchiv Nordrhein-Westfalen.</summary>
      </format>
      <format>
         <puid type="fmt">1376</puid>
         <name>xdomea 2.0.1</name>
         <summary>Changed xdomea from uppercase to lowercase. Submitted by Landesarchiv Nordrhein-Westfalen.</summary>
      </format>
      <format>
         <puid type="fmt">1377</puid>
         <name>xdomea 2.1.0</name>
         <summary>Changed xdomea from uppercase to lowercase. Submitted by Landesarchiv Nordrhein-Westfalen.</summary>
      </format>
      <format>
         <puid type="fmt">1378</puid>
         <name>xdomea 2.2.0</name>
         <summary>Changed xdomea from uppercase to lowercase. Submitted by Landesarchiv Nordrhein-Westfalen.</summary>
      </format>
      <format>
         <puid type="fmt">1379</puid>
         <name>xdomea 2.3.0</name>
         <summary>Changed xdomea from uppercase to lowercase. Submitted by Landesarchiv Nordrhein-Westfalen.</summary>
      </format>
      <format>
         <puid type="fmt">1380</puid>
         <name>xdomea 2.4.0</name>
         <summary>Changed xdomea from uppercase to lowercase. Submitted by Landesarchiv Nordrhein-Westfalen.</summary>
      </format>
      <format>
         <puid type="fmt">1454</puid>
         <name>Web Video Text Tracks (WebVTT) Format</name>
         <summary>Added links to documentation, expanded sig and des. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="fmt">1693</puid>
         <name>Asymetrix Compel File 1</name>
         <summary>Removed priority with fmt/470 and added extension .art. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1694</puid>
         <name>Asymetrix Compel File 2</name>
         <summary>Removed priority with fmt/470 and added extension .art. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="x-fmt">44</puid>
         <name>WordPerfect for MS-DOS/Windows Document 6.x</name>
         <summary>Changed version from 6.0 to 6.x as the signature was previously for v6.1 to chatch all variations of version 6. Updated signature and signature note. Added extensions w61 and w62. Submitted by Brigham Young University and Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="x-fmt">66</puid>
         <name>Microsoft Access Database File 2.0</name>
         <summary>Updated file format name, signature and description, added extension .mda. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="x-fmt">102</puid>
         <name>3D Studio (DOS) 2D Shape File</name>
         <summary>Expanded name from '3D Studio Shapes' to '3D Studio (DOS) 2D Shape File', added internal sig, description and note. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="x-fmt">120</puid>
         <name>Microsoft Works for Windows 4.0</name>
         <summary>Deprecation of the format in favour of fmt/233. Submitted by Preservica.</summary>
      </format>
      <format>
         <puid type="x-fmt">146</puid>
         <name>Scitex Continuous Tone Bitmap</name>
         <summary>New extension .sct added. Submitted by The Church of Jesus Christ of Latter-Day Saints and Preservica.</summary>
      </format>
      <format>
         <puid type="x-fmt">216</puid>
         <name>Microsoft Powerpoint Packaged Presentation</name>
         <summary>Added vendor, source, description, developer, support, internal signature and prioroity over x-fmt/414. Submitted by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="x-fmt">238</puid>
         <name>Microsoft Access Database File 95</name>
         <summary>Updated description and name, added extensions .mda, .mdt and .mde, added notes, identifiers and developer. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="x-fmt">239</puid>
         <name>Microsoft Access Database File 97</name>
         <summary>Updated description and name, added extensions .mda, .mdt and .mde, added notes, identifiers and developer. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="x-fmt">240</puid>
         <name>Microsoft Access Database File 2000</name>
         <summary>Updated description and name, added extension .mde, added notes, identifiers and developer. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="x-fmt">241</puid>
         <name>Microsoft Access Database File 2002</name>
         <summary>Updated description and name, added extension .mde, added notes, identifiers and developer. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="x-fmt">394</puid>
         <name>WordPerfect for MS-DOS/Windows Document 5.1</name>
         <summary>Added priority over fmt/1280 NCH Dictation Audio File. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="x-fmt">411</puid>
         <name>Windows Portable Executable</name>
         <summary>Added Portable Executable Format document, notes field updated. Submitted by Earldridge Jazzed Pineda .</summary>
      </format>
   </release_outline>
   <release_outline name="New Signatures">
      <format>
         <puid type="fmt">1794</puid>
         <name>JPEG 2000 Codestream</name>
         <summary>Signature researched and samples provided by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1795</puid>
         <name>Asymetrix Toolbook File 6-11.5</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1796</puid>
         <name>Wireless Markup Language (WML) Document</name>
         <summary>Signature researched and samples provided by Stadtarchiv Hof.</summary>
      </format>
      <format>
         <puid type="fmt">1798</puid>
         <name>CHAT Transcription Format</name>
         <summary>Signature researched and samples provided by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1799</puid>
         <name>FLExText Interlinear XML Format</name>
         <summary>Signature researched and samples provided by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1800</puid>
         <name>Multimedia Viewer Book</name>
         <summary>Signature researched and samples provided by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1801</puid>
         <name>Praat TextGrid</name>
         <summary>Signature researched and samples provided by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1802</puid>
         <name>Transcriber AG TAG Format</name>
         <summary>Signature researched and samples provided by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1803</puid>
         <name>Transcriber TRS Format</name>
         <summary>Signature researched and samples provided by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1805</puid>
         <name>Microsoft Access Database File 1.0</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1806</puid>
         <name>Microsoft Access Database File 1.1</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1807</puid>
         <name>Microsoft Access Encrypted Database File 1.0</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1808</puid>
         <name>Microsoft Access Encrypted Database File 1.1</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1809</puid>
         <name>Microsoft Access Encrypted Database File 2.0</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1810</puid>
         <name>Raw PIMA SWIR Reflectance Spectral File</name>
         <summary>Signature researched and samples provided by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">1811</puid>
         <name>Vips Image</name>
         <summary>Signature researched and samples provided by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1812</puid>
         <name>Audio Data Transport Stream</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1813</puid>
         <name>xdomea 3.0.0</name>
         <summary>Signature researched and samples provided by Landesarchiv Nordrhein-Westfalen.</summary>
      </format>
      <format>
         <puid type="fmt">1814</puid>
         <name>Adobe Color Book for Windows</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1816</puid>
         <name>Adobe Swatch Exchange</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1817</puid>
         <name>Direct Stream Digital Stream File</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1818</puid>
         <name>Direct Stream Digital Interchange File Format</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1819</puid>
         <name>MacCaption File 1</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1820</puid>
         <name>MacCaption File 2</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1821</puid>
         <name>MacCaption Project</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1822</puid>
         <name>Audacity Audio Block File</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1823</puid>
         <name>Audacity Project File Early</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1824</puid>
         <name>Audacity Project File 1.x</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1825</puid>
         <name>Audacity Project File 2.x</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1826</puid>
         <name>Audacity Project File 3.x</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1827</puid>
         <name>DOCX Strict OOXML Document</name>
         <summary>Signature researched and samples provided by Danish National Archives and Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1828</puid>
         <name>XLSX Strict OOXML Spreadsheet</name>
         <summary>Signature researched and samples provided by Danish National Archives and Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1829</puid>
         <name>PPTX Strict OOXML Presentation</name>
         <summary>Signature researched and samples provided by Danish National Archives and Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1830</puid>
         <name>3D Studio (DOS) 2D/3D Loft Object File</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1831</puid>
         <name>3D Studio (DOS) Project File</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1832</puid>
         <name>ArcSoft PhotoStudio File</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1833</puid>
         <name>ArcSoft Album and SlideShow Files for PhotoStudio and PhotoImpression</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1834</puid>
         <name>GoDot 4Bit Graphics Format</name>
         <summary>Signature researched and samples provided by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1835</puid>
         <name>Archiver Format</name>
         <summary>Signature researched and samples provided by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1836</puid>
         <name>Brio Query File</name>
         <summary>Signature researched and samples provided by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1837</puid>
         <name>WordPerfect Presentations</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1838</puid>
         <name>Leica Project File</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1839</puid>
         <name>Microsoft Publisher Packaged Document</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1840</puid>
         <name>WACZ</name>
         <summary>Signature researched and samples provided by The National Archives and Records Administration and Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1841</puid>
         <name>Digital Negative Format (DNG) 1.5</name>
         <summary>Signature researched and samples provided by .</summary>
      </format>
      <format>
         <puid type="fmt">1842</puid>
         <name>Digital Negative Format (DNG) 1.6</name>
         <summary>Signature researched and samples provided by .</summary>
      </format>
      <format>
         <puid type="fmt">1843</puid>
         <name>Human Machine Interfaces HMI File</name>
         <summary>Signature researched and samples provided by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1844</puid>
         <name>GNU Image Manipulation Program Palette File</name>
         <summary>Signature researched and samples provided by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">118</puid>
         <name>Windows Bitmap 4.0</name>
         <summary>Signature researched and samples provided by GoldFynch eDiscovery.</summary>
      </format>
      <format>
         <puid type="fmt">119</puid>
         <name>Windows Bitmap 5.0</name>
         <summary>Signature researched and samples provided by GoldFynch eDiscovery.</summary>
      </format>
      <format>
         <puid type="fmt">1215</puid>
         <name>ERDAS Hierarchical File Architecture Format/Reduced Resolution Dataset</name>
         <summary>Signature researched and samples provided by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">1218</puid>
         <name>SubRip Subtitle File</name>
         <summary>Signature researched and samples provided by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1288</puid>
         <name>IESNA LM-63 Photometric Data File</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1314</puid>
         <name>GL Transmission Format (Text) 1.x</name>
         <summary>Signature researched and samples provided by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1315</puid>
         <name>GL Transmission Format (Text) 2.x</name>
         <summary>Signature researched and samples provided by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">1454</puid>
         <name>Web Video Text Tracks (WebVTT) Format</name>
         <summary>Signature researched and samples provided by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="x-fmt">44</puid>
         <name>WordPerfect for MS-DOS/Windows Document 6.x</name>
         <summary>Signature researched and samples provided by Brigham Young University and Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="x-fmt">66</puid>
         <name>Microsoft Access Database File 2.0</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="x-fmt">102</puid>
         <name>3D Studio (DOS) 2D Shape File</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
      <format>
         <puid type="x-fmt">216</puid>
         <name>Microsoft Powerpoint Packaged Presentation</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-Day Saints.</summary>
      </format>
   </release_outline>
</release_note>
<release_note>
   <release_date>1st November 2022</release_date>
   <signature_filename>DROID_SignatureFile_V109.xml</signature_filename>
   <release_outline name="New Records">
      <format>
         <puid type="fmt">1767</puid>
         <name>Calc602 Project File v1.51</name>
         <summary>Full entry added. Submitted by The National Archives of the Czech Republic.</summary>
      </format>
      <format>
         <puid type="fmt">1768</puid>
         <name>C Source Code File</name>
         <summary>Extension-only entry added. Submitted by Stadtarchiv Hof.</summary>
      </format>
      <format>
         <puid type="fmt">1769</puid>
         <name>C++ Source Code File</name>
         <summary>Extension-only entry added. Submitted by Stadtarchiv Hof.</summary>
      </format>
      <format>
         <puid type="fmt">1770</puid>
         <name>GenBank Flat File</name>
         <summary>Full entry added. Submitted by Bodleian Libraries.</summary>
      </format>
      <format>
         <puid type="fmt">1771</puid>
         <name>ESRI Persistent Auxiliary Metadata File</name>
         <summary>Full entry added. Submitted by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">1772</puid>
         <name>Casio QV CAM</name>
         <summary>Full entry added. Submitted by The Church of Jesus Christ of Latter-day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1773</puid>
         <name>Calc602 Spreadsheet File</name>
         <summary>Full entry added. Submitted by The National Archives of the Czech Republic.</summary>
      </format>
      <format>
         <puid type="fmt">1774</puid>
         <name>602 Graph/Chart File</name>
         <summary>Full entry added. Submitted by The National Archives of the Czech Republic.</summary>
      </format>
      <format>
         <puid type="fmt">1775</puid>
         <name>Calc602 Project File</name>
         <summary>Full entry added. Submitted by The National Archives of the Czech Republic.</summary>
      </format>
      <format>
         <puid type="fmt">1776</puid>
         <name>Extensible Markup Language v1.1</name>
         <summary>Full entry added. Submitted by Stadtarchiv Hof.</summary>
      </format>
      <format>
         <puid type="fmt">1777</puid>
         <name>SIARD (Software-Independent Archiving of Relational Databases)</name>
         <summary>Full entry added. Submitted by Swiss Federal Archives.</summary>
      </format>
      <format>
         <puid type="fmt">1778</puid>
         <name>Dynamic Publisher Picture File</name>
         <summary>Full entry added. Submitted by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1779</puid>
         <name>Dynamic Publisher Font File</name>
         <summary>Full entry added. Submitted by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1780</puid>
         <name>Koala MicroIllustrator Graphic File</name>
         <summary>Full entry added. Submitted by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1781</puid>
         <name>Pentax PEF Image File</name>
         <summary>Full entry added. Submitted by The Church of Jesus Christ of Latter-day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1782</puid>
         <name>The Spectral Geologist Dataset v7.15</name>
         <summary>Full entry added. Submitted by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">1783</puid>
         <name>The Spectral Geologist Dataset v7</name>
         <summary>Full entry added. Submitted by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">1784</puid>
         <name>Animatic Film Format</name>
         <summary>Full entry added. Submitted by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1785</puid>
         <name>FLR Database File</name>
         <summary>Full entry added. Submitted by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1786</puid>
         <name>Funpaint Image File</name>
         <summary>Full entry added. Submitted by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1787</puid>
         <name>G9B Graphics Format Bitmap</name>
         <summary>Full entry added. Submitted by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1788</puid>
         <name>Gunpaint Image File</name>
         <summary>Full entry added. Submitted by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1789</puid>
         <name>GX2 Graphics File</name>
         <summary>Full entry added. Submitted by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1790</puid>
         <name>Help Librarian File</name>
         <summary>Full entry added. Submitted by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1791</puid>
         <name>Haiku Vector Icon Format</name>
         <summary>Full entry added. Submitted by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1792</puid>
         <name>ICDRAW Single Icon File</name>
         <summary>Full entry added. Submitted by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1793</puid>
         <name>ICDRAW Group Icon File</name>
         <summary>Full entry added. Submitted by The National Archives and Records Administration.</summary>
      </format>
   </release_outline>
   <release_outline name="Updated Records">
      <format>
         <puid type="fmt">41</puid>
         <name>Raw JPEG Stream</name>
         <summary>Updated description and reference links, added extensions jif; jfif; jfi, and LoC identifier. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="fmt">42</puid>
         <name>JPEG File Interchange Format v1.00</name>
         <summary>Updated reference links, added extensions jif; jfif; jfi. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="fmt">43</puid>
         <name>JPEG File Interchange Format v1.01</name>
         <summary>Updated reference links, added extensions jif; jfif; jfi. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="fmt">44</puid>
         <name>JPEG File Interchange Format v1.02</name>
         <summary>Updated reference links, added extensions jif; jfif; jfi, and LoC identifier. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="fmt">123</puid>
         <name>Encapsulated PostScript File Format v2.0</name>
         <summary>Adjusted signature to allow for 3 wildcard bytes in the EPS 2.0 signature instead of 2. Submitted by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">142</puid>
         <name>Waveform Audio (WAVEFORMATEX)</name>
         <summary>Adjusted signature caused by copying error from previous release. Submitted by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">198</puid>
         <name>MPEG Audio Stream Layer II</name>
         <summary>Removed comma from name, updated description, reference links, added relationships and LoC identifier. Submitted by Preservica.</summary>
      </format>
      <format>
         <puid type="fmt">330</puid>
         <name>Peak Graphical Waveform File</name>
         <summary>Changed filetype to Audio. Submitted by National Library of the Netherlands.</summary>
      </format>
      <format>
         <puid type="fmt">462</puid>
         <name>MS-DOS Compression Format (SZDD Variant)</name>
         <summary>Changed filetype to Aggregate. Submitted by National Library of the Netherlands.</summary>
      </format>
      <format>
         <puid type="fmt">1062</puid>
         <name>Hasselblad 3FR Raw Image</name>
         <summary>Added updated and previously removed signature in v94 of PRONOM. Updated description and reference links. . Submitted by The Church of Jesus Christ of Latter-day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1241</puid>
         <name>FO File</name>
         <summary>Updated signature and MIME type. Submitted by The National Archives of the Czech Republic.</summary>
      </format>
      <format>
         <puid type="fmt">1242</puid>
         <name>ZFO (Form) File</name>
         <summary>Updated container signature name and sequence. Submitted by The National Archives of the Czech Republic.</summary>
      </format>
      <format>
         <puid type="fmt">1697</puid>
         <name>Calc602 Spreadsheet file v1.51</name>
         <summary>Added priority over fmt/1773, name adjusted and corrected error in signature description. Submitted by The National Archives of the Czech Republic.</summary>
      </format>
      <format>
         <puid type="fmt">1698</puid>
         <name>Calc602 Spreadsheet file v1.00</name>
         <summary>Added priority over fmt/1773, name adjusted. Submitted by The National Archives of the Czech Republic.</summary>
      </format>
      <format>
         <puid type="fmt">1699</puid>
         <name>602 Graph/Chart File v1.51</name>
         <summary>Added priority over fmt/1774. Submitted by The National Archives of the Czech Republic.</summary>
      </format>
      <format>
         <puid type="fmt">1713</puid>
         <name>Calc602 Project File v1.0</name>
         <summary>Added priority over fmt/1775. Submitted by The National Archives of the Czech Republic.</summary>
      </format>
      <format>
         <puid type="fmt">1739</puid>
         <name>UDF-ISO 9660 Bridge Disc</name>
         <summary>Priority added over fmt/1738 due to copying error from previous release. Submitted by Digital Preservation Department, The National Archives.</summary>
      </format>
      <format>
         <puid type="x-fmt">62</puid>
         <name>Log File</name>
         <summary>Updated description. Submitted by Stadtarchiv Hof.</summary>
      </format>
      <format>
         <puid type="x-fmt">422</puid>
         <name>Java Language Source Code File</name>
         <summary>Updated description and capitalised name. Submitted by Stadtarchiv Hof.</summary>
      </format>
   </release_outline>
   <release_outline name="New Signatures">
      <format>
         <puid type="fmt">1767</puid>
         <name>Calc602 Project File v1.51</name>
         <summary>Signature researched and samples provided by The National Archives of the Czech Republic.</summary>
      </format>
      <format>
         <puid type="fmt">1770</puid>
         <name>GenBank Flat File</name>
         <summary>Signature researched and samples provided by Bodleian Libraries.</summary>
      </format>
      <format>
         <puid type="fmt">1771</puid>
         <name>ESRI Persistent Auxiliary Metadata File</name>
         <summary>Signature researched and samples provided by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">1772</puid>
         <name>Casio QV CAM</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1773</puid>
         <name>Calc602 Spreadsheet File</name>
         <summary>Signature researched and samples provided by The National Archives of the Czech Republic.</summary>
      </format>
      <format>
         <puid type="fmt">1774</puid>
         <name>602 Graph/Chart File</name>
         <summary>Signature researched and samples provided by The National Archives of the Czech Republic.</summary>
      </format>
      <format>
         <puid type="fmt">1775</puid>
         <name>Calc602 Project File</name>
         <summary>Signature researched and samples provided by The National Archives of the Czech Republic.</summary>
      </format>
      <format>
         <puid type="fmt">1776</puid>
         <name>Extensible Markup Language v1.1</name>
         <summary>Signature researched and samples provided by Stadtarchiv Hof.</summary>
      </format>
      <format>
         <puid type="fmt">1777</puid>
         <name>SIARD (Software-Independent Archiving of Relational Databases)</name>
         <summary>Signature researched and samples provided by Swiss Federal Archives.</summary>
      </format>
      <format>
         <puid type="fmt">1778</puid>
         <name>Dynamic Publisher Picture File</name>
         <summary>Signature researched and samples provided by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1779</puid>
         <name>Dynamic Publisher Font File</name>
         <summary>Signature researched and samples provided by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1780</puid>
         <name>Koala MicroIllustrator Graphic File</name>
         <summary>Signature researched and samples provided by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1781</puid>
         <name>Pentax PEF Image File</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1782</puid>
         <name>The Spectral Geologist Dataset v7.15</name>
         <summary>Signature researched and samples provided by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">1783</puid>
         <name>The Spectral Geologist Dataset v7</name>
         <summary>Signature researched and samples provided by The National Library of Australia.</summary>
      </format>
      <format>
         <puid type="fmt">1784</puid>
         <name>Animatic Film Format</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1785</puid>
         <name>FLR Database File</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-day Saints.</summary>
      </format>
      <format>
         <puid type="fmt">1786</puid>
         <name>Funpaint Image File</name>
         <summary>Signature researched and samples provided by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1787</puid>
         <name>G9B Graphics Format Bitmap</name>
         <summary>Signature researched and samples provided by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1788</puid>
         <name>Gunpaint Image File</name>
         <summary>Signature researched and samples provided by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1789</puid>
         <name>GX2 Graphics File</name>
         <summary>Signature researched and samples provided by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1790</puid>
         <name>Help Librarian File</name>
         <summary>Signature researched and samples provided by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1791</puid>
         <name>Haiku Vector Icon Format</name>
         <summary>Signature researched and samples provided by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1792</puid>
         <name>ICDRAW Single Icon File</name>
         <summary>Signature researched and samples provided by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1793</puid>
         <name>ICDRAW Group Icon File</name>
         <summary>Signature researched and samples provided by The National Archives and Records Administration.</summary>
      </format>
      <format>
         <puid type="fmt">1062</puid>
         <name>Hasselblad 3FR Raw Image</name>
         <summary>Signature researched and samples provided by The Church of Jesus Christ of Latter-day Saints.</summary>
      </format>
   </release_outline>
</release_note>
</release_notes>
"""


def test_parse_xml():
    """Ensure the main function for the template repository exists."""
    release_summary = parse_release_xml(release_xml=RELEASE_XML)
    assert release_summary.date == "2023-08-22"
    assert release_summary.latest_puid == "fmt/1900"
    assert release_summary.version == "V114"


def test_parse_release_dates():
    """Ensure parsing release dates works as expected."""
    assert parse_release_date("1st May 2023") == "2023-05-01"
    assert parse_release_date("22nd August 2023") == "2023-08-22"
    assert parse_release_date("10th May 2023") == "2023-05-10"
    assert parse_release_date("16th March 2023") == "2023-03-16"
    assert parse_release_date("14th March 2023") == "2023-03-14"
    assert parse_release_date("1st November 2022") == "2022-11-01"


def test_parse_http_dates():
    """Ensure that HTTP header dates are parsed correctly."""
    http_date = parse_http_date("Tue, 22 Aug 2023 13:42:05 GMT")
    assert str(http_date.date()) == "2023-08-22"


def test_parse_signature_file_string():
    """Ensure we can get a signature file version from the release notes"""
    assert parse_signature_file_string("DROID_SignatureFile_V114.xml") == "V114"
    assert parse_signature_file_string("DROID_SignatureFile_V112.xml") == "V112"
    assert parse_signature_file_string("DROID_SignatureFile_V111.xml") == "V111"
    assert parse_signature_file_string("DROID_SignatureFile_V110.xml") == "V110"
    assert parse_signature_file_string("DROID_SignatureFile_V109.xml") == "V109"
