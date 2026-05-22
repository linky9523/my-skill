---
name: product-info-house
description: Use when product planning teammates need to turn product facts, PRDs, meeting notes, white papers, sell-point tables, launch materials, or public product pages into a product information house for internal alignment, decks, white papers, or image generation. Produce concise Chinese positioning, core value, three pillars, evidence, risks, Image2-ready prompts, and generator-ready JSON.
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
- If the user asks to make an image, prepare the information house JSON first, then call Image2 to generate the final delivery image when Image2 is available.
- If Image2 is not available or lacks credentials, return the JSON plus an Image2-ready prompt instead of using another image path.

## Interactive Intake

When the user has not provided enough structured material, guide them step by step instead of asking for a full brief at once.

Default question order:

1. 产品名称与版本
2. 屋顶定位: one sentence about the desired product recognition
3. 核心价值: why users choose it
4. 用户价值: 2-3 user outcomes or scenarios
5. 产品能力: 2-3 confirmed capabilities, parameters, or technologies
6. 传播表达: 2-3 storylines, copy angles, or material needs
7. 证据支撑: official pages, specs, samples, tests, certifications, PRD fields, or meeting confirmations
8. 风险与待补: missing evidence, expression boundaries, legal risks, or unclear versions

Ask only the next useful question. If the user says to generate now, infer conservatively from what is available and put gaps in `risks`.

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
6. After generating, provide self-check suggestions unless the user explicitly asks for JSON only.

## Image2 Generation

Use Image2 for final image generation when the user asks for a delivery image, poster, diagram, or "生成图".

Process:

1. Build and self-check the information house JSON first.
2. Read `references/brand_visual_oppo.md` when:
   - the product is OPPO, OnePlus/一加 under OPPO context, or OPPO-facing work
   - the user does not provide a color or visual direction
   - the user asks for OPPO brand visual consistency
3. If no color is provided, default to OPPO green and white.
4. Call Image2 with a prompt that includes:
   - the complete product information house content
   - green/white OPPO visual theme unless overridden
   - clear house structure: roof, core value, three pillars, foundation evidence, foundation risk/todo
   - instruction to keep Chinese text legible and faithful
   - instruction not to invent claims, parameters, certifications, awards, or extreme statements
5. After Image2 returns the image, inspect the result conceptually:
   - text is legible
   - structure is still a product information house
   - no invented claims were added
   - default OPPO green/white style is respected
   - risk/todo is visible but not visually dominant

Do not use the local web generator as the default image path unless the user specifically asks for the local generator.

## Self-Check Suggestions

After generation, check and briefly suggest fixes for:

- positioning or core value too long for a diagram
- fewer than 2 points or more than 4 points in any pillar
- weak or missing evidence
- uncertain claims placed in `evidence` instead of `risks`
- extreme words or unconditional effect promises
- version mismatch or unclear product edition
- missing samples, tests, certifications, or official source references

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

For OPPO/default visual rules, read `references/brand_visual_oppo.md`.
