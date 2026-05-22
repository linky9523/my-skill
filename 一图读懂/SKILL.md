---
name: product-infographic-excel
description: Turn product source files into a poster-like Chinese product "一图读懂" Excel wireframe for product planning. Use when the user provides official website copy, selling-point tables, PRDs, launch notes, product specs, screenshots, or reference long images and asks for an 一图读懂, 长图框架, 海报式表格排版, 卖点框架, 信息层级表, or Excel handoff for designers rather than a finished visual design.
---

# Product Infographic Excel

## Goal

Create a product-planning Excel handoff that looks like a poster wireframe inside a spreadsheet. The first sheet must let designers understand the rough long-image layout at a glance: KV area, section titles, image placeholders, selling-point cards, proof lines, and visual-material needs.

This is not a finished design file and not a channel/sales sheet. Do not include default price, package, preorder, sale time, QR, channel, or legal footer blocks unless the user explicitly asks for them.

## Inputs

Accept any mix of:

- Official website exports, selling-point tables, PRDs, launch notes, spec sheets, product decks, screenshots, or reference "一图读懂" images.
- User notes about priority, target audience, tone, launch positioning, required selling points, and material availability.

If reference images are available, inspect them for structure and hierarchy only. Extract how they arrange KV, core KSP cards, scenario/sample sections, capability sections, system/screen/performance/battery sections, and footnote-like remarks. Ignore price/package/sales blocks by default.

## Workflow

1. Read source files and collect a compact source map:
   - product name, machine setting/positioning, slogan/tagline
   - must-have selling points and proof parameters
   - user benefits and scenario language
   - visual/material clues, sample image needs, CG/device/screenshot needs
   - uncertain specs, source conflicts, and design dependencies
2. Build a limited-length "一图读懂" story:
   - KV: product name, brand/co-branding, positioning, hero visual
   - Core promise: one sentence that frames the product value
   - Highlights/KSP: keep the strongest 3 cards in the main poster
   - Thematic sections: usually 3-4 sections total after KV, grouped by user value
   - Experience sections: combine secondary specs into compact grids; move long-tail points to `文案与素材清单`
3. Write copy in planner style:
   - Level 1: section headline, short and memorable
   - Level 2: selling-point title, capability plus user benefit
   - Level 3: proof line, parameters, feature names, scenarios
   - Body: concise explanation only when needed
   - Notes: mark TBD, needs parameter confirmation, source conflict, or design dependency
4. Prepare one JSON file matching `references/json-schema.md`, then run `scripts/build_infographic_excel.py`.
5. Verify the first sheet visually. It should feel like a rough poster made from table cells, not like a database table.

## Output Workbook

Include these sheets:

- `海报式排版`: the primary deliverable. Use a vertical long-image canvas made from merged cells, section bands, card groups, and image placeholders. Keep it close to a normal 一图读懂 length, using `一图读懂-启明星.jpg` style density as the reference: KV plus about 3-4 major content sections, not a full website-length page.
- `文案与素材清单`: editable list of all section copy, proof points, sources, and material needs.
- `待确认项`: missing parameters, risky claims, source conflicts, and design/material dependencies.

The first sheet should use:

- Large merged blocks for KV and major image areas.
- White cards for selling points.
- Pale color blocks for image/CG/sample placeholders.
- Section titles between modules.
- Short text that directly maps to poster hierarchy.

## Product-Planning Boundary

Exclude by default:

- SKU price tables
- package/accessory sales bundles
- preorder or sale-time copy
- channel, QR, booking, purchase, campaign mechanics
- legal footers unrelated to product claims

If these appear in sources, either ignore them or put a brief note in `待确认项` only when they affect product copy. Do not make them poster modules.

## Quality Bar

- Prioritize layout clarity over spreadsheet completeness.
- The first sheet must be understandable without reading the other sheets.
- Keep the first sheet short: default to no more than 4 modules after KV and no more than 3 visible cards per module. Put extra selling points in `文案与素材清单`, not the poster canvas.
- Keep one selling point per card. Split overloaded rows.
- Every high-impact claim should have a proof point, parameter, source, or `待确认`.
- Do not invent specs. If a claim is likely but not confirmed, mark it in `待确认项`.
- Preserve official feature names unless the user asks for copy polishing.
- Make the first draft useful even when sources are incomplete: use image placeholders and open questions instead of blocking.

## Reference Files

- Read `references/json-schema.md` before creating the structured JSON for the builder script.
- Read `references/patterns.md` when deciding module order, copy hierarchy, or rough layout.

## Script

Use:

```bash
python3 /path/to/product-infographic-excel/scripts/build_infographic_excel.py input.json output.xlsx
```

The script creates a poster-like Excel workbook and filters out default non-product-planning modules such as price, package, preorder, sale time, and channel blocks.
