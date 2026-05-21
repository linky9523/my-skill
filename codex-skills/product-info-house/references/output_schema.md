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
- `pillars[].points`: 2 to 4 short points per pillar.
- `evidence`: 2 to 5 items.
- `risks`: 2 to 5 items.

## Quality Bar

- Do not invent product data.
- Put uncertain claims in `risks`, not in `evidence`.
- Keep diagram text compact.
- Use "待补充" when evidence is missing.
