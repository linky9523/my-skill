# Product Info House Skill

面向产品策划团队的“产品信息屋”复用包，用来把产品资料、会议纪要、PRD、卖点表整理成可放入汇报图的结构。

## 包含内容

- `codex-skills/product-info-house`: Codex skill，可安装到同事的 Codex skills 目录。
- `chatgpt-product-info-house-prompt.md`: 给只用 ChatGPT 的同事使用的一句话提示词。
- `team-reuse-plan.md`: 团队复用方式。
- `install-product-info-house-skill.sh`: 本机安装脚本。

## 安装 Codex Skill

```bash
zsh install-product-info-house-skill.sh
```

安装后可以在 Codex 中使用：

```text
请使用 product-info-house skill，把这份产品资料整理成产品信息屋，并输出可粘贴进生成器的 JSON。
```

## ChatGPT 同事

打开 `chatgpt-product-info-house-prompt.md`，复制里面的简化提示词，把产品资料粘到最后即可。
