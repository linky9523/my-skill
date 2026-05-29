---
name: 写备注skill
description: 为产品策划官网文案表、卖点表、参数表或官网框架表生成一一对应的官网备注。用于读取 .xlsx 表格、参考既有备注库或人工备注，在每个适用 sheet 最右侧新增备注生成列，只为广告法风险、功能限制、数据口径、认证、防水、AI、配件另售、样片演示等必要场景写合规备注。
---

# 写备注skill

## Workflow

1. Read the workbook structure first: sheet names, header rows, existing remark columns, merged ranges, and representative rows.
2. Read the reference library or existing remarks when provided. Use exact existing remarks when they already fit; otherwise synthesize concise remarks from the same risk category.
3. Add generated remarks in the rightmost available column of each applicable sheet. Keep the original table and any existing remark columns unchanged.
4. Default to `/` for ordinary content rows. Only write a remark when the row has a standalone legal/compliance risk, a human remark already exists, or the row uses a footnote marker.
5. When a remark is needed, name the exact object being limited: e.g. `进光量数据`, `AI 一键闪记`, `卫星通信功能`, `4K 超清实况功能`, `相关配件或套装`. Avoid vague category text such as `相关对比、提升或行业表述`, and never write `xxx 为页面卖点表述`.
6. If multiple rows share the same `屏数`, avoid repeating the same remark line. Keep the first occurrence within that screen and use `/` when a later row has no new remark content.
7. Preserve row order and avoid merging cells in the generated remark column unless the source table already requires it.
8. Export a new workbook copy rather than overwriting the source file.

## Remark Rules

Load [references/official-website-remark-patterns.md](references/official-website-remark-patterns.md) before drafting remarks manually.

Write remarks only for:

- Existing human remarks or explicit footnote markers such as `（12）`.
- Specific comparison or uplift claims with a clear measured object and comparison scope, such as lens light intake, pixel uplift, GPU power, memory usage, or battery cycle life.
- Feature availability limits caused by model, software version, region, account login, network, app support, operator support, switch setting, or later OTA.
- Certification, medical-adjacent, eye-care, waterproof/dustproof/drop-proof, satellite/operator, AI-generated, third-party service, accessory/kit sold separately, or sample photo/video claims.

Do not repeat generic OPPO laboratory-source wording on every row. Put broad data-source, UI-reference, AI-effect, and product-image caveats into the final global note unless a row has a specific comparison, uplift, certification, or condition-sensitive claim. Pure objective parameters such as `最高达 224MB/s`, ordinary refresh rates, capacity values, and similar figures usually do not need row-level remarks.

Remarks are not a cure for absolute or superlative advertising-law risk. If a row only says `最高`, `首款`, `行业领先`, or similar but no concrete note can be written, use `/`; the copy itself should be reviewed separately.

Do not treat chip names such as `电池管理芯片` as battery claims. Write battery remarks only for clear capacity, charging, battery life, cycle-life, typical/rated value, or low-temperature battery-performance claims. Avoid loose keyword matches such as treating `抢票成功率` as `功率`.

Bad: `相关对比、提升或行业表述基于特定测试条件或统计口径...`

Bad: `“AI 灵感成片 AI 补光...”为页面卖点表述，涉及行业、首发、独家、最高或领先等判断时...`

Good: `主摄镜头进光量数据来自 OPPO 实验室，相关提升或对比结果基于页面所述测试对象及测试条件，因测试环境、方法、软件版本、设备状态等不同，数据可能存在差异，请以产品实际为准。`

## Automation

Use `scripts/generate_official_remarks.py` for repeated spreadsheet work:

```bash
python scripts/generate_official_remarks.py input.xlsx --output output.xlsx
```

The script detects header rows, reads existing `备注`/`文案备注` columns, creates a rightmost `备注生成` column, and writes row-aligned remarks.
