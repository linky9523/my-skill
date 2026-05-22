---
name: product-info-house
description: Use when product planning teammates need to turn product facts, PRDs, meeting notes, white papers, sell-point tables, launch materials, or public product pages into a product information house for internal alignment, decks, white papers, or the local generator. Produce concise Chinese positioning, core value, three pillars, evidence, risks, and generator-ready JSON.
---

# Product Info House

Convert scattered product information into a reusable "产品信息屋" structure for product planning work.

## Core Output

Always produce a structure with:

- 产品名称
- 一句话产品定位
- 核心价值
- 三根信息支柱
- 证据支撑
- 风险与待补
- 可复制 JSON

The JSON must follow the schema in `references/output_schema.md` so it can be pasted into the local generator.

## Output Mode

- If the user asks for "JSON", "粘贴到生成器", "做图", or "只要结果", return only valid JSON inside a fenced code block.
- If the user asks for exploration or review, give a short readable summary first, then JSON.
- If the user asks to make an image and the local generator is available, prepare generator-ready JSON first, then use the generator workflow.

## Workflow

1. Read the user's material and identify the product version, target user, scene, capabilities, proof, and missing facts.
2. Separate facts from interpretation:
   - Facts: official names, parameters, features, test data, certifications, samples, user scenarios explicitly stated.
   - Interpretation: value, positioning, copy angles, launch narrative, inferred user benefits.
3. Build the house:
   - Roof: one positioning sentence.
   - Core value: why users choose it.
   - Three pillars: "用户价值", "产品能力", "传播表达" by default.
   - Foundation: evidence and risks/todos.
4. Run the risk check before final output.
5. Keep every claim grounded. Mark missing evidence as "待补充" or "待确认"; do not invent data.

## Information Selection

- Prioritize facts that support a clear user choice, not every available parameter.
- Prefer 2-3 points per pillar for a clean diagram; use 4 only when the product is complex.
- Put numbers in "产品能力" or "证据支撑"; put user outcomes in "用户价值".
- Put copy directions,素材建议, and launch angles in "传播表达".
- If several versions exist, name the exact version used. If version is unclear, add a risk item.
- If public/current product information is needed and the user did not provide enough material, verify from official sources when available.

## House Logic

- 屋顶: product positioning. One clear sentence about who the product is for and what recognition it should build.
- 核心价值: the user-facing reason to choose the product.
- 三根支柱: the three strongest support routes for the positioning.
- 地基: evidence, test data, samples, certifications, competitive facts, and risk/todo checks.

## Writing Rules

- Write in Chinese by default.
- Be specific, but do not over-polish into advertising copy.
- Prefer short phrases that fit inside a diagram:
  - `positioning`: ideally under 28 Chinese characters.
  - `coreValue`: ideally under 36 Chinese characters.
  - `pillars[].points`: ideally under 24 Chinese characters when possible.
- If source information is messy, preserve uncertainty with labels such as "待确认", "待补测试数据", or "需补样张".
- If a field is absent, infer conservatively and show what needs to be supplemented.
- Avoid making "传播表达" sound like final ad copy unless the user asks for marketing copy.

## Risk Checks

Before finalizing, check:

- 极限词: 首, 最, 唯一, 顶级, 行业第一, 绝对, 全场景.
- 效果承诺: charging time, waterproofing, battery life, durability, camera results, AI performance, or any broad promise.
- 参数规范: units, capitalization, spacing, model names, color names, feature names.
- Evidence gaps: claims without samples, tests, certifications, data, or product-team confirmation.
- Version mismatch: product name, edition, region, launch date, or spec page does not match the claim.

## Evidence Rules

- Evidence can include official pages, PRD fields, parameter tables, test reports, certifications, user research, samples, and confirmed meeting notes.
- Do not place inferred benefits in `evidence`.
- If evidence is weak, write the claim as a todo or risk instead of upgrading it into a fact.

## Copyable Prompt For Generator

When the user wants a generator-ready output, return only valid JSON inside a fenced code block. Do not include comments in the JSON.

For stricter field rules, read `references/output_schema.md`.
