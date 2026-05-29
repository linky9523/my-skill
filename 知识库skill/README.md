# 知识库 Skill

这个 Skill 用来帮助团队把某个项目的资料沉淀成一个本地知识库。团队成员可以把产品信息、卖点表、竞品资料、会议纪要、历史交付件等放进统一目录，之后让 AI 优先基于这些资料回答、总结、提炼或生成交付件。

## 推荐知识库位置

默认放在当前业务工作区：

```text
knowledge_base/projects/{project_name}/
```

示例：

```text
knowledge_base/projects/Find_X10e/
```

如果你的仓库已经有固定资料目录，请优先沿用现有目录规范。

## 推荐目录结构

```text
knowledge_base/
└── projects/
    └── {project_name}/
        ├── project_index.md
        ├── 01_product_info/
        ├── 02_selling_points/
        ├── 03_competitors/
        ├── 04_user_research/
        ├── 05_marketing_outputs/
        ├── 06_meeting_notes/
        └── 99_archive/
```

## 每个目录放什么

- `01_product_info`：产品基础信息、定位、参数、版本、价格、上市节奏。
- `02_selling_points`：卖点信息表、功能说明、用户收益、技术解释、传播表达。
- `03_competitors`：竞品资料、价格配置对比、竞品卖点、传播打法分析。
- `04_user_research`：用户调研、访谈纪要、评论分析、目标人群洞察。
- `05_marketing_outputs`：官网框架、PPT、发布会文案、门店话术、社媒内容、培训材料。
- `06_meeting_notes`：会议纪要、评审意见、关键决策、修改记录。
- `99_archive`：过期资料、旧版本文件、已废弃方案。

## 使用方法

建立项目知识库时，可以这样说：

```text
使用 $知识库skill 为 Find X10e 建立项目知识库。
```

基于知识库提问时，可以这样说：

```text
使用 $知识库skill 基于 Find X10e 的项目知识库，总结这个项目的核心卖点。
```

更新资料时，可以这样说：

```text
使用 $知识库skill 我新增了一份竞品分析文件，请帮我判断放在哪里，并更新项目索引。
```

## 两个模板

- `knowledge_base_template.md`：给团队看的资料放置规则和命名规则。
- `project_index_template.md`：每个项目的 `project_index.md` 初始模板。

## 注意事项

- 没有资料依据时，不要让 AI 编造产品事实。
- 旧版本资料应放入 `99_archive`，不要默认当成最新口径。
- 如果资料之间冲突，应先列出冲突点，再让项目负责人确认。
- 默认不联网搜索；只有用户明确要求时才查外部信息。
- 保密资料只在本地或用户指定环境中处理，不要主动上传到外部平台。
