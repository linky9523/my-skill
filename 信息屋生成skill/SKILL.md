---
name: product-info-house
description: Use when product planning teammates need to turn product facts, PRDs, meeting notes, white papers, sell-point tables, launch materials, or public product pages into a product information house for internal alignment, decks, white papers, or Image2 generation. First identify the information-house type and whether the user already has a hierarchy; then collect content layer by layer, self-check, ask whether to optimize, and generate images directly with Image2 when available.
---

# Product Info House

Convert scattered product information into a reusable "产品信息屋" structure for product planning work.

## Core Output

Produce a structure with:

- 产品名称
- 信息屋类型
- 用户确认或系统建议的层级架构
- 每一层的标题、层级、内容
- 证据支撑, when relevant
- 风险与待补, when relevant or requested
- 自查建议
- 可复制 JSON

Use the schema guidance in `references/output_schema.md`. Do not force the default three-pillar product house when the user provides a different hierarchy.

## Output Mode

- If the user asks for "JSON", "粘贴到生成器", or "只要结果", return only valid JSON inside a fenced code block.
- If the user asks for exploration or review, give a short readable summary first, then JSON.
- If the user asks to make an image, prepare and self-check the information house JSON first, then call Image2 directly when image generation is available in the current Codex environment.
- Do not return an Image2 prompt when Image2/image generation is available. Return an Image2-ready prompt only when the image-generation capability is unavailable or blocked.

## Interactive Intake

When the user has not provided enough structured material, guide them step by step instead of asking for a full brief at once.

Start with these two questions before collecting layer content:

1. 信息屋类型: examples include 产品卖点信息屋, 发布传播信息屋, 影像能力信息屋, AI 功能信息屋, 素材规划信息屋, 风险审核信息屋, or a user-defined type.
2. 层级架构是否清晰:
   - If yes, ask the user to provide the hierarchy, then collect content one layer at a time.
   - If no, ask for the product/material context and propose 1-2 hierarchy options based on the information-house type. Wait for the user to choose or edit before collecting content.

Layer collection rules:

- Ask only the next useful question.
- Follow the user's hierarchy names exactly unless they ask for polishing.
- For each layer, collect title, level/role, and content bullets.
- Ask for evidence only when the current layer contains factual claims, parameters, capability names, effect claims, or claims likely to be used externally.
- Ask for risks/todos only when the user wants review, when claims lack evidence, or when there are expression boundaries. If the user explicitly says risks are not needed, omit the risk layer from the image but keep any safety concerns in self-check suggestions outside the image.
- If the user says to generate now, infer conservatively from what is available and put gaps in self-check suggestions or `risks` when risks are allowed.

Suggested hierarchy examples when the user has no hierarchy:

- 产品卖点信息屋: 屋顶定位 -> 核心价值 -> 用户价值/产品能力/传播表达 -> 证据支撑 -> 风险与待补
- 发布传播信息屋: 传播主线 -> 用户心智 -> 核心信息 -> 场景素材 -> 证据与审核边界
- AI 功能信息屋: 用户任务 -> AI 能力 -> 使用场景 -> 体验收益 -> 证据与限制
- 素材规划信息屋: 内容目标 -> 关键画面 -> 样张/视频/商详素材 -> 责任人与排期 -> 缺口与风险

## Workflow

1. Identify the information-house type and hierarchy status before collecting detailed content.
2. If hierarchy is clear, follow it. If not, propose a hierarchy based on the type and ask the user to confirm.
3. Read the user's material and identify the product version, target user, scene, capabilities, proof, and missing facts.
4. Separate facts from interpretation:
   - Facts: official names, parameters, features, test data, certifications, samples, user scenarios explicitly stated.
   - Interpretation: value, positioning, copy angles, launch narrative, inferred user benefits.
5. Build the house according to the confirmed hierarchy. Use the default product-house structure only when the user chooses it or has no better hierarchy.
6. Run the self-check before final output.
7. Keep every claim grounded. Mark missing evidence as "待补充" or "待确认"; do not invent data.
8. After generating, provide self-check suggestions unless the user explicitly asks for JSON only. Ask whether the user wants the skill to optimize the information house based on those suggestions.

## Image2 Generation

Use Image2 for final image generation when the user asks for a delivery image, poster, diagram, or "生成图".

Process:

1. Build and self-check the information house JSON first.
2. Check whether image generation/Image2 is available in the current Codex environment.
   - If available, call it directly. Do not merely return a prompt.
   - If unavailable, state the blocker briefly and return an Image2-ready prompt.
3. Read `brand_visual_oppo.md` when:
   - the product is OPPO, OnePlus/一加 under OPPO context, or OPPO-facing work
   - the user does not provide a color or visual direction
   - the user asks for OPPO brand visual consistency
4. If no color is provided, default to OPPO green and white.
5. Call Image2 with a prompt that includes:
   - the complete product information house content
   - green/white OPPO visual theme unless overridden
   - the confirmed house hierarchy and layer names
   - instruction to keep Chinese text legible and faithful
   - instruction not to invent claims, parameters, certifications, awards, or extreme statements
6. After Image2 returns the image, inspect the result conceptually:
   - text is legible
   - structure follows the confirmed hierarchy
   - no invented claims were added
   - default OPPO green/white style is respected
   - risk/todo is included only when requested or relevant

Do not use the local web generator as the default image path unless the user specifically asks for the local generator.

## Self-Check Suggestions

After generation, check and briefly suggest fixes for:

- whether the output follows the user's chosen information-house type
- whether the hierarchy is clear, complete, and non-overlapping
- whether any layer title or content is too long for a diagram
- whether a layer has too few or too many bullets
- weak or missing evidence
- uncertain claims placed in `evidence` instead of `risks`
- extreme words or unconditional effect promises
- version mismatch or unclear product edition
- missing samples, tests, certifications, or official source references

After listing suggestions, ask: "需要我按这些建议优化一版吗？" Do not optimize silently unless the user has asked for automatic optimization.

## Information Selection

- Prioritize facts that support a clear user choice, not every available parameter.
- Prefer 2-3 points per pillar for a clean diagram; use 4 only when the product is complex.
- Put numbers in "产品能力" or "证据支撑"; put user outcomes in "用户价值".
- Put copy directions,素材建议, and launch angles in "传播表达".
- If several versions exist, name the exact version used. If version is unclear, add a risk item.
- If public/current product information is needed and the user did not provide enough material, verify from official sources when available.

## House Logic

- For user-defined hierarchy, preserve the user's layer logic.
- For default product-house hierarchy:
  - 屋顶: product positioning. One clear sentence about who the product is for and what recognition it should build.
  - 核心价值: the user-facing reason to choose the product.
  - 三根支柱: the three strongest support routes for the positioning.
  - 地基: evidence, test data, samples, certifications, competitive facts, and optional risk/todo checks.

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

For OPPO/default visual rules, read `brand_visual_oppo.md`.
