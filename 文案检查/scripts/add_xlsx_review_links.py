#!/usr/bin/env python3
"""Add visible internal navigation links to the review-record sheet of an XLSX."""

from __future__ import annotations

import argparse
import copy
import re
import shutil
import tempfile
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

MAIN = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PKG_REL = "http://schemas.openxmlformats.org/package/2006/relationships"
NS = {"x": MAIN, "r": REL, "pr": PKG_REL}
ET.register_namespace("", MAIN)
ET.register_namespace("r", REL)


def cell_text(cell: ET.Element, shared: list[str]) -> str:
    cell_type = cell.get("t")
    if cell_type == "inlineStr":
        return "".join(cell.itertext())
    value = cell.find("x:v", NS)
    if value is None or value.text is None:
        return ""
    if cell_type == "s":
        return shared[int(value.text)]
    return value.text


def shared_strings(zf: zipfile.ZipFile) -> list[str]:
    try:
        root = ET.fromstring(zf.read("xl/sharedStrings.xml"))
    except KeyError:
        return []
    return ["".join(si.itertext()) for si in root.findall("x:si", NS)]


def sheet_part(zf: zipfile.ZipFile, sheet_name: str) -> str:
    workbook = ET.fromstring(zf.read("xl/workbook.xml"))
    rels = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
    relationships = {rel.get("Id"): rel.get("Target") for rel in rels.findall("pr:Relationship", NS)}
    for sheet in workbook.findall("x:sheets/x:sheet", NS):
        if sheet.get("name") == sheet_name:
            target = relationships[sheet.get(f"{{{REL}}}id")]
            normalized = target.lstrip("/")
            return normalized if normalized.startswith("xl/") else f"xl/{normalized}"
    raise ValueError(f"Worksheet not found: {sheet_name}")


def add_links(input_path: Path, output_path: Path, review_sheet: str, start_row: int, location_col: str) -> int:
    with zipfile.ZipFile(input_path) as src:
        part = sheet_part(src, review_sheet)
        shared = shared_strings(src)
        root = ET.fromstring(src.read(part))
        sheet_data = root.find("x:sheetData", NS)
        if sheet_data is None:
            raise ValueError("Review worksheet has no sheetData.")

        links = []
        pattern = re.compile(r"^(.+)!([A-Z]{1,3}[1-9][0-9]*)$")
        for cell in sheet_data.findall(".//x:c", NS):
            ref = cell.get("r", "")
            match_ref = re.match(r"([A-Z]+)([0-9]+)", ref)
            if not match_ref or match_ref.group(1) != location_col or int(match_ref.group(2)) < start_row:
                continue
            label = cell_text(cell, shared)
            match_label = pattern.match(label)
            if not match_label:
                continue
            target_sheet, target_cell = match_label.groups()
            escaped = target_sheet.replace("'", "''")
            links.append((ref, f"'{escaped}'!{target_cell}", label))

        existing = root.find("x:hyperlinks", NS)
        if existing is not None:
            root.remove(existing)
        hyperlinks = ET.Element(f"{{{MAIN}}}hyperlinks")
        for ref, location, label in links:
            ET.SubElement(
                hyperlinks,
                f"{{{MAIN}}}hyperlink",
                {"ref": ref, "location": location, "display": label},
            )
        ext_lst = root.find("x:extLst", NS)
        position = list(root).index(ext_lst) if ext_lst is not None else len(root)
        root.insert(position, hyperlinks)
        new_xml = ET.tostring(root, encoding="utf-8", xml_declaration=True)

        with tempfile.TemporaryDirectory() as tmp:
            temp_output = Path(tmp) / output_path.name
            with zipfile.ZipFile(temp_output, "w", zipfile.ZIP_DEFLATED) as dst:
                for info in src.infolist():
                    data = new_xml if info.filename == part else src.read(info.filename)
                    dst.writestr(copy.copy(info), data)
            shutil.copyfile(temp_output, output_path)
    return len(links)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_xlsx", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--sheet", default="审查记录")
    parser.add_argument("--start-row", type=int, default=5)
    parser.add_argument("--column", default="B")
    args = parser.parse_args()
    count = add_links(args.input_xlsx, args.out, args.sheet, args.start_row, args.column)
    print(f"Added {count} internal review links.")


if __name__ == "__main__":
    main()
