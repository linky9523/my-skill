# Product Info House Output Schema

Use this JSON shape for the local product information house generator.

```json
{
  "productName": "产品名称",
  "positioning": "一句话产品定位",
  "coreValue": "用户为什么选择它",
  "pillars": [
    {
      "title": "用户价值",
      "points": ["要点 1", "要点 2", "要点 3"]
    },
    {
      "title": "产品能力",
      "points": ["要点 1", "要点 2", "要点 3"]
    },
    {
      "title": "传播表达",
      "points": ["要点 1", "要点 2", "要点 3"]
    }
  ],
  "evidence": ["证据、参数、样张、测试、认证或竞品对比"],
  "risks": ["风险点、待确认事项、缺失证据或表达边界"]
}
```

## Field Rules

- `productName`: use the official product or project name if available.
- `positioning`: one sentence, preferably under 28 Chinese characters.
- `coreValue`: one user-facing value sentence, preferably under 36 Chinese characters.
- `pillars`: exactly 3 pillars for the default house layout.
- `pillars[].title`: default to "用户价值", "产品能力", "传播表达" unless the user requests a custom structure.
- `pillars[].points`: 2 to 4 short points per pillar; 2 to 3 is preferred for image output.
- `evidence`: 2 to 5 items.
- `risks`: 2 to 5 items.

## Quality Bar

- Do not invent product data.
- Put uncertain claims in `risks`, not in `evidence`.
- Keep diagram text compact.
- Use "待补充" when evidence is missing.
- Keep product version names consistent across the whole JSON.
- Do not include comments, markdown, trailing commas, or extra keys in the JSON.

## Placement Guide

- Put user scenarios, pain points, and outcomes in "用户价值".
- Put parameters, functions, technology, certifications, and confirmed capabilities in "产品能力".
- Put copy angles, storylines, material needs, and review reminders in "传播表达".
- Put official pages, PRD fields, parameter tables, test reports, certifications, samples, and confirmed meeting notes in `evidence`.
- Put missing samples, missing tests, version ambiguity, legal expression boundaries, and unverified claims in `risks`.
