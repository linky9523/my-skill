---
name: write-remarks
description: Generate one-to-one official website disclaimer remarks for product planning spreadsheets, especially mobile phone website copy tables in .xlsx files. Use when Codex needs to read product page copy, selling points, parameters, image/video/sample requirements, or existing remark libraries and add a rightmost remarks column with compliance-style notes for each corresponding row.
---

# Write Remarks

## Workflow

1. Read the workbook structure first: sheet names, header rows, existing remark columns, merged ranges, and representative rows.
2. Read the reference library or existing remarks when provided. Use exact existing remarks when they already fit; otherwise synthesize concise remarks from the same risk category.
3. Add generated remarks in the rightmost available column of each applicable sheet. Keep the original table and any existing remark columns unchanged.
4. Write one remark cell per content row. Use `/` only when the row has content but no standalone remark is needed.
5. Preserve row order and avoid merging cells in the generated remark column unless the source table already requires it.
6. Export a new workbook copy rather than overwriting the source file.

## Remark Rules

Load [references/official-website-remark-patterns.md](references/official-website-remark-patterns.md) before drafting remarks manually.

Prefer remarks that cover:

- Source or measurement conditions for lab data, supplier data, test data, or comparative uplift.
- Feature availability limits caused by software version, region, account login, network, app support, or later OTA.
- Photo, sample, video, screen, UI, and generated image effects being for reference only.
- Battery, charging, waterproofing, durability, accessory, storage, and communication conditions.
- Camera focal length, pixels, zoom, sensor, aperture, stabilization, color, HDR, Log, and shooting mode constraints.

Do not turn remarks into marketing copy. Keep them factual, scoped, and close to the claim in the same row.

## Automation

Use `scripts/generate_official_remarks.py` for repeated spreadsheet work:

```bash
python scripts/generate_official_remarks.py input.xlsx --output output.xlsx
```

The script detects header rows, reads existing `备注`/`文案备注` columns, creates a rightmost `备注生成` column, and writes row-aligned remarks.
