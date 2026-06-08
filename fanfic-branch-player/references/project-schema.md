# 项目文件协议

## 目录

```text
项目目录/
├── project.json
├── 原作基线.md
├── 改写目标.md
├── branch-tree.json
├── 世界线状态.md
├── 创作日志.md
└── 剧情/
```

所有 JSON 文件使用 UTF-8 和 2 空格缩进。正文与人工确认信息使用 Markdown。

## project.json

关键字段：

| 字段 | 含义 |
| --- | --- |
| `schema_version` | 当前固定为 `1` |
| `project_id` | 初始化时生成，不随改名变化 |
| `source.title` | 原作名称 |
| `source.input_mode` | `title` 或 `upload` |
| `source.files` | 用户提供的原作文件路径列表 |
| `mode` | V1 固定为 `director` |
| `current_node_id` | 当前世界线节点 |
| `next_node_number` | 下一个稳定节点序号 |
| `preferences` | 视角、场景长度、偏好和禁忌 |

## branch-tree.json

`nodes` 是以节点 ID 为键的对象。每个节点包含：

- `id`：稳定 ID，格式为 `n0000`、`n0001`。
- `parent_id`：父节点；根节点为 `null`。
- `children`：直接子节点 ID。
- `choice`：从父节点进入本节点的用户选择。
- `title`、`scene_file`、`summary`。
- `state_snapshot`：该节点完整且独立的世界线状态。
- `options`：本节点结束时提供给用户的候选选择。
- `ending`：是否为结局节点。
- `created_at`：UTC ISO 8601 时间。

回溯依赖每个节点的完整快照，禁止只保存一份全局可变状态。

## 世界线状态

推荐结构：

```json
{
  "characters": {},
  "relationships": {},
  "facts": [],
  "secrets": {},
  "promises": [],
  "open_conflicts": []
}
```

可以按作品增加字段。`project_tools.py add-node` 使用 JSON Merge Patch：

- 对象递归合并。
- `null` 删除对应字段。
- 数组和其他值整体替换。

`世界线状态.md` 是当前节点快照的可读镜像，不是独立真相源；切换节点时由脚本重写。

## 命令

### 初始化

```bash
python3 scripts/project_tools.py init <project-dir> \
  --source-title "作品名" \
  --input-mode title \
  --branch-point "切入节点"
```

可选参数：

- `--source-file <path>`：可重复，上传原作时记录来源。
- `--perspective <value>`：默认 `第三人称`。
- `--scene-min 800 --scene-max 1500`。

### 登记节点

```bash
python3 scripts/project_tools.py add-node <project-dir> \
  --parent n0000 \
  --choice "选择摘要" \
  --title "标题" \
  --scene "剧情/n0001-标题.md" \
  --summary "结果摘要" \
  --state-patch '{"facts":["新的已确认事实"]}' \
  --options '[{"label":"A","action":"行动","cost":"代价","opens":"方向"}]'
```

`--state-patch` 和 `--options` 也接受以 `@` 开头的 JSON 文件路径，例如 `@patch.json`。

### 回溯与检查

```bash
python3 scripts/project_tools.py list <project-dir>
python3 scripts/project_tools.py checkout <project-dir> --node n0001
python3 scripts/project_tools.py validate <project-dir>
```

`checkout` 只切换当前节点和可读状态镜像，不删除任何分支。
