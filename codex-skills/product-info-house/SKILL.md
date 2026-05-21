---
name: product-info-house
description: Use when product planning teammates need to turn product facts, PRDs, meeting notes, white papers, sell-point tables, or launch materials into a product information house structure for internal alignment, decks, white papers, or the local product information house generator. Produce concise Chinese outputs with positioning, core value, three pillars, evidence, and risks.
---

# Product Info House

Use this skill to help product planning teams convert scattered product information into a reusable "产品信息屋" structure.

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

## Workflow

1. Read the user's material.
2. Separate product facts from marketing interpretation.
3. Extract the target user, product positioning, core value, main capabilities, evidence, and risks.
4. Build exactly three information pillars unless the user explicitly asks for another structure.
5. Keep every claim grounded in the provided material.
6. Mark missing evidence as "待补充", rather than inventing data.
7. Avoid extreme claims such as "最", "唯一", "第一", "行业领先" unless the source includes clear evidence.
8. End with JSON only when the user wants to paste into the generator; otherwise include a short readable summary first, then JSON.

## House Logic

- 屋顶: product positioning. One clear sentence about who the product is for and what recognition it should build.
- 核心价值: the user-facing reason to choose the product.
- 三根支柱: the three strongest support routes for the positioning.
- 地基: evidence, test data, samples, certifications, competitive facts, and risk/todo checks.

## Writing Rules

- Write in Chinese by default.
- Be specific, but do not over-polish into advertising copy.
- Prefer short phrases that can fit inside a diagram.
- If source information is messy, preserve uncertainty with labels such as "待确认", "待补测试数据", or "需补样张".
- If a field is absent, infer conservatively and show what needs to be supplemented.

## Risk Checks

Before finalizing, check:

- 极限词: 首, 最, 唯一, 顶级, 行业第一, 绝对, 全场景.
- 效果承诺: charging time, waterproofing, battery life, durability, camera results, AI performance, or any broad promise.
- 参数规范: units, capitalization, spacing, model names, color names, feature names.
- Evidence gaps: claims without samples, tests, certifications, data, or product-team confirmation.

## Copyable Prompt For Generator

When the user wants a generator-ready output, return only valid JSON inside a fenced code block. Do not include comments in the JSON.
