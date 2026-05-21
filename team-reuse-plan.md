# 团队复用方案

## 方案 A：同事也用 Codex

把下面这个文件夹复制到同事的 Codex skills 目录：

```text
codex-skills/product-info-house
```

同事之后可以这样说：

```text
请使用 product-info-house skill，把这份产品资料整理成产品信息屋，并输出可粘贴进生成器的 JSON。
```

然后把 JSON 粘贴到本地 `index.html` 的输入框里，点击“生成信息屋”。

## 方案 B：同事只用 ChatGPT

把这个文件发给同事：

```text
chatgpt-product-info-house-prompt.md
```

同事复制里面的“一句话生成产品信息屋”提示词，把产品资料粘到最后，让 ChatGPT 输出 JSON。熟悉后也可以只用文件底部的“更短口令”。

然后把 JSON 粘贴到本地 `index.html` 的输入框里，点击“生成信息屋”。

## 推荐试点流程

1. 选一个真实项目，不要选最复杂的旗舰项目。
2. 准备一份产品信息表、会议纪要或卖点材料。
3. 让 Codex 或 ChatGPT 输出信息屋 JSON。
4. 粘贴到本地工具生成图片。
5. 由产品策划人工微调定位、核心价值和风险项。
6. 把图片放进内部讨论材料，观察是否能减少对齐成本。
