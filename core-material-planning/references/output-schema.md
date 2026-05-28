# Output Schema

Create a JSON object with these fields before running the Excel builder.

```json
{
  "product": {
    "name": "OPPO Reno16",
    "positioning": "打开实况想象力，我有我的生命力",
    "colors": ["怦然星动", "星河紫", "月夜黑"],
    "source": "https://www.oppo.com/cn/smartphones/series-reno/reno16/"
  },
  "materials": [
    {
      "category": "KV",
      "detail": "产品 KV",
      "description": "OPPO Reno16 全色 KV",
      "phone_display": "全色",
      "quantity": "1",
      "priority": "重点素材"
    }
  ],
  "confirmations": [
    {
      "item": "AI 一键闪记屏幕素材",
      "reason": "官网确认功能，但未给出最终演示 UI 与素材截屏",
      "suggestion": "确认是否使用 ColorOS 官方 UI 截图或重新录制",
      "related_material": "启动 AI 一键闪记（竖屏握持）"
    }
  ]
}
```

## Field Rules

- `product.name`: product name used in workbook title.
- `product.positioning`: slogan or product positioning.
- `product.colors`: official confirmed color names. Use this to calculate base quantities.
- `product.source`: source URL or file name. Put source detail in the summary only, not as a main-list column.
- `materials`: required list for `核心素材清单`.
- `materials[].category`: output to `素材分类`.
- `materials[].detail`: output to `需求细则`.
- `materials[].description`: output to `需求说明`.
- `materials[].phone_display`: output to `手机展现`; use `TBD` when not confirmed.
- `materials[].quantity`: output to `需求数量`; keep values as strings such as `1`, `3`, `8*3`.
- `materials[].priority`: output to `优先级`; use `重点素材`, `新增`, `TBD`, or blank.
- `confirmations`: optional list for `待确认项`.
- `confirmations[].item`: unresolved item title.
- `confirmations[].reason`: why it is unresolved.
- `confirmations[].suggestion`: what to verify next.
- `confirmations[].related_material`: related row or feature.

## Main Sheet Contract

The builder writes only these six columns to `核心素材清单`:

1. `素材分类`
2. `需求细则`
3. `需求说明`
4. `手机展现`
5. `需求数量`
6. `优先级`

Never add `参考` to `materials` or the main sheet.

## Row Granularity

Each object in `materials` must represent one concrete material requirement. Do not combine several shots, angles, camera components, or scenarios into a single `description`.

For example, write eight-view product renders as eight `materials` rows with the same `category` and `detail`, one row each for `纯正面`, `纯背面`, `顶面`, `底面`, `左45度正`, `右45度正`, `左45度背`, and `右45度背`. The Excel builder will visually merge repeated `素材分类` and `需求细则` cells.
