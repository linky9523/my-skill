# JSON Schema Guide

Create a UTF-8 JSON file with this shape before running `scripts/build_infographic_excel.py`.

Do not include price, package bundle, preorder, sale time, QR, channel, or purchase mechanics unless the user explicitly asks.

The first sheet is length-limited by default. Even if `modules` contains many sections and many selling points, the poster canvas should show only the first 4 non-KV product-planning modules and the first 3 cards per module. The full content still appears in `文案与素材清单`.

```json
{
  "product": {
    "name": "OPPO Find X9 Ultra",
    "positioning": "口袋哈苏",
    "slogan": "光学至上 口袋哈苏",
    "audience": "影像旗舰用户",
    "tone": "专业、清晰、克制"
  },
  "source_files": [
    {"file": "官网信息.xlsx", "note": "官网卖点与参数"}
  ],
  "modules": [
    {
      "order": 1,
      "section": "KV",
      "screen": "1",
      "section_title": "OPPO Find X9 Ultra",
      "subtitle": "光学至上 口袋哈苏",
      "purpose": "建立产品名称、机设和视觉记忆",
      "layout": "顶部大 KV，产品图占主要面积，标题居中",
      "visual": "产品 KV / co-brand logo / 主视觉",
      "copy_blocks": [
        {"level": "一级标题", "text": "OPPO Find X9 Ultra", "source": "官网"},
        {"level": "二级标题", "text": "光学至上 口袋哈苏", "source": "官网"}
      ],
      "selling_points": [],
      "notes": "如无 KV 图，标注产品图占位"
    },
    {
      "order": 2,
      "section": "Highlights",
      "screen": "2",
      "section_title": "远近明暗都清晰",
      "subtitle": "一屏先打透最强影像卖点：大长焦 + 双 2 亿 + 色彩 + 视频",
      "purpose": "一屏概览最强卖点",
      "layout": "1 个主卡 + 2-4 个辅助卡 + 样张带",
      "visual": "爆炸图、样张、器件图组合",
      "copy_blocks": [],
      "selling_points": [
        {
          "title": "哈苏 10 倍光变天眼长焦",
          "benefit": "把「望远镜」装进手机",
          "proof": "支持 20 倍光学品质变焦 | 最高 120 倍数字变焦",
          "parameters": "20x, 120x",
          "visual": "长焦器件图 / 五反光路 CG",
          "source": "卖点表",
          "notes": "参数需按最终官网口径确认"
        }
      ],
      "notes": ""
    }
  ],
  "source_facts": [
    {
      "topic": "影像",
      "fact": "哈苏 10 倍光变天眼长焦",
      "source": "官网信息.xlsx",
      "confidence": "高",
      "notes": ""
    }
  ],
  "open_questions": [
    {
      "item": "ColorOS 版本",
      "owner": "产品",
      "reason": "源文件存在不同表达",
      "suggested_action": "确认最终官网口径"
    }
  ]
}
```

## Field Rules

- `modules` is the poster sequence. Keep module order identical to the planned long image.
- Put the most important modules and cards first. The poster sheet is intentionally compressed; overflow belongs in `文案与素材清单`.
- `section_title` and `subtitle` appear directly on the poster sheet.
- `layout` and `visual` become design-facing placeholders.
- `copy_blocks` is for section-level copy not tied to one card.
- `selling_points` is for repeated cards inside a module.
- Use `notes` for TBD, source conflicts, or design/material dependencies.
- `source_facts` should be auditable but compact.
- If a field is unknown, use an empty string and add an `open_questions` item.
