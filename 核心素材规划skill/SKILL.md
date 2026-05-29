---
name: core-material-planning
description: Plan core visual material lists for smartphone products from product facts, selling-point tables, launch notes, official product pages, PRDs, or rough feature briefs. Use when Codex needs to turn phone positioning, CMF/design, imaging, performance, battery, AI, connectivity, durability, or scenario selling points into an Excel-ready core material plan with categories, shot/detail needs, phone/color display, quantities, priorities, and confirmation items.
---

# Core Material Planning

## Goal

Turn smartphone product information into a production-facing core material plan. The default deliverable is an Excel workbook with a `核心素材清单` sheet and a `待确认项` sheet.

The main list must use exactly these columns:

- `素材分类`
- `需求细则`
- `需求说明`
- `手机展现`
- `需求数量`
- `优先级`

Do not create a `参考` column. Treat reference images, URLs, or examples as planning evidence only.

## Inputs

Accept any mix of:

- Product name, positioning, slogan, launch angle, target audience, hero narrative.
- Color/CMF/version information.
- Selling points by design, screen, imaging, performance, battery, charging, communication, AI, OS, durability, accessories, or scenario.
- Official website copy, spec tables, PRDs, launch notes, decks, screenshots, or prior material lists.
- User notes about must-have materials, excluded materials, available phones, required colors, schedule, or priorities.

When public/current product information is needed and the user gives a URL, verify from the URL first. Do not invent specs or feature names.

## Workflow

1. Extract a compact product source map:
   - product name, slogan, positioning, key launch story
   - colors/versions and which colors are confirmed
   - core selling points and proof parameters
   - scene claims and user scenarios
   - uncertain items, missing execution details, and source conflicts
2. Read `references/material-planning-rules.md` before mapping selling points to material needs.
3. Draft the core material plan:
   - include fixed base materials first
   - map design, hardware, and scenario selling points to rows
   - use one row for one concrete material requirement; split product angles, camera components, and scenarios instead of packing several needs into one row
   - mark hero/differentiated/visually provable rows as `重点素材`
   - use `TBD` when phone/color display or execution details are unknown
4. Put unresolved information in `待确认项`, not in invented row detail.
5. Prepare a JSON file matching `references/output-schema.md`.
6. Run `scripts/build_core_material_plan_excel.py input.json output.xlsx`.
7. Open or inspect the workbook enough to confirm:
   - no `参考` column exists
   - `核心素材清单` and `待确认项` sheets exist
   - base rows and key selling-point rows are present
   - color-based quantities are correct, especially `8*颜色数`

## Planning Defaults

- Use Chinese by default.
- Keep `需求说明` execution-oriented and concise.
- Use the product's official feature names when available.
- Default base rows include product KV, eight-view product renders, single-color CMF still life, all-color combination still life, packaging/open-box image, and basic hand model scenes.
- For colors, use official color names in `手机展现` when confirmed. Use `全色` for KV and color-combination rows.
- For eight-view product renders, create eight separate rows. Each row uses the color count as `需求数量`; the Excel output visually merges repeated big-title cells.
- For one-off feature rows, default quantity is `1` unless the selling point clearly needs multiple scenes/focal lengths/colors.
- If a row needs CG, structure diagrams, sample photos, real phones, cross-device props, or environment setup but the source does not confirm details, record it in `待确认项`.

## Output Rules

- Keep the main sheet focused on planning rows, not commentary.
- Do not include source URLs, long evidence paragraphs, or execution remarks in the main sheet unless the user asks.
- Do not create price, channel, preorder, package sales, QR code, or campaign mechanics rows unless the user explicitly requests sales/channel materials.
- Do not over-expand every website feature. Prioritize materials that help produce launch/KV/product-detail visual assets.
- If a source has many minor software features, group them into a small number of representative AI/OS/interaction rows and add confirmation notes for exact screen/demo assets.
- Use an OPPO-inspired green and white Excel theme by default: clean white canvas, OPPO green title/header accents, soft-green grouped cells, dark gray body text, and restrained warm labels for priority/todo.

## References

- `references/material-planning-rules.md`: selling-point to material mapping rules.
- `references/output-schema.md`: JSON shape for the Excel builder.

## Script

Use:

```bash
python3 /path/to/core-material-planning/scripts/build_core_material_plan_excel.py input.json output.xlsx
```

The script creates an Excel workbook with `核心素材清单` and `待确认项` and preserves the six-column main-sheet contract.
