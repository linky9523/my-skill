#!/usr/bin/env python3
"""Create and maintain branch-safe interactive fan-fiction projects."""

from __future__ import annotations

import argparse
import copy
import json
import re
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SCHEMA_VERSION = 1
NODE_RE = re.compile(r"^n\d{4,}$")


def now_utc() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"缺少文件：{path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"JSON 无法解析：{path}: {exc}") from exc


def write_json(path: Path, value: Any) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def parse_json_argument(raw: str, label: str) -> Any:
    if raw.startswith("@"):
        source = Path(raw[1:]).expanduser()
        raw = source.read_text(encoding="utf-8")
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"{label} 不是有效 JSON：{exc}") from exc


def merge_patch(target: Any, patch: Any) -> Any:
    """Apply RFC 7396-style JSON Merge Patch semantics."""
    if not isinstance(patch, dict):
        return copy.deepcopy(patch)
    if not isinstance(target, dict):
        target = {}
    result = copy.deepcopy(target)
    for key, value in patch.items():
        if value is None:
            result.pop(key, None)
        elif isinstance(value, dict):
            result[key] = merge_patch(result.get(key), value)
        else:
            result[key] = copy.deepcopy(value)
    return result


def default_state() -> dict[str, Any]:
    return {
        "characters": {},
        "relationships": {},
        "facts": [],
        "secrets": {},
        "promises": [],
        "open_conflicts": [],
    }


def markdown_value(value: Any, indent: int = 0) -> list[str]:
    pad = "  " * indent
    if isinstance(value, dict):
        if not value:
            return [f"{pad}- （暂无）"]
        lines: list[str] = []
        for key, child in value.items():
            if isinstance(child, (dict, list)):
                lines.append(f"{pad}- **{key}**")
                lines.extend(markdown_value(child, indent + 1))
            else:
                lines.append(f"{pad}- **{key}**：{child}")
        return lines
    if isinstance(value, list):
        if not value:
            return [f"{pad}- （暂无）"]
        lines = []
        for item in value:
            if isinstance(item, (dict, list)):
                lines.append(f"{pad}-")
                lines.extend(markdown_value(item, indent + 1))
            else:
                lines.append(f"{pad}- {item}")
        return lines
    return [f"{pad}- {value}"]


def render_state(project_dir: Path, node_id: str, state: dict[str, Any]) -> None:
    lines = [
        "# 当前世界线状态",
        "",
        f"- 当前节点：`{node_id}`",
        "- 此文件由 `project_tools.py` 根据节点快照生成；请勿将它作为唯一存档。",
        "",
    ]
    labels = {
        "characters": "人物状态",
        "relationships": "人物关系",
        "facts": "已确认事实",
        "secrets": "秘密与信息差",
        "promises": "承诺",
        "open_conflicts": "未解决冲突",
    }
    ordered_keys = list(labels)
    ordered_keys.extend(key for key in state if key not in labels)
    for key in ordered_keys:
        lines.append(f"## {labels.get(key, key)}")
        lines.append("")
        lines.extend(markdown_value(state.get(key, {})))
        lines.append("")
    (project_dir / "世界线状态.md").write_text("\n".join(lines), encoding="utf-8")


def load_project(project_dir: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    project = read_json(project_dir / "project.json")
    tree = read_json(project_dir / "branch-tree.json")
    return project, tree


def command_init(args: argparse.Namespace) -> None:
    project_dir = Path(args.project_dir).expanduser().resolve()
    if project_dir.exists() and any(project_dir.iterdir()):
        raise ValueError(f"目标目录不是空目录：{project_dir}")
    project_dir.mkdir(parents=True, exist_ok=True)
    (project_dir / "剧情").mkdir()

    project_id = str(uuid.uuid4())
    root_id = "n0000"
    created_at = now_utc()
    state = default_state()
    source_files = [str(Path(item).expanduser().resolve()) for item in args.source_file]
    project = {
        "schema_version": SCHEMA_VERSION,
        "project_id": project_id,
        "source": {
            "title": args.source_title,
            "input_mode": args.input_mode,
            "files": source_files,
        },
        "mode": "director",
        "current_node_id": root_id,
        "next_node_number": 1,
        "preferences": {
            "perspective": args.perspective,
            "scene_length": {"min": args.scene_min, "max": args.scene_max},
            "pairing": "",
            "tone": "",
            "avoid": [],
        },
        "created_at": created_at,
        "updated_at": created_at,
    }
    tree = {
        "schema_version": SCHEMA_VERSION,
        "root_node_id": root_id,
        "nodes": {
            root_id: {
                "id": root_id,
                "parent_id": None,
                "children": [],
                "choice": None,
                "title": "原作分歧点",
                "scene_file": None,
                "summary": args.branch_point,
                "state_snapshot": state,
                "options": [],
                "ending": False,
                "created_at": created_at,
            }
        },
    }
    write_json(project_dir / "project.json", project)
    write_json(project_dir / "branch-tree.json", tree)
    render_state(project_dir, root_id, state)
    (project_dir / "原作基线.md").write_text(
        f"""# 原作基线

## 确认状态

- 状态：待用户确认
- 原作：{args.source_title}
- 输入方式：{args.input_mode}

## 已确认事实

- 待填写

## 关键人物与核心动机

- 待填写

## 当前关系

- 待填写

## 节点前已发生事件

- 待填写

## 世界规则

- 待填写

## 待确认与版本差异

- 待填写

## 来源位置

- 待填写
""",
        encoding="utf-8",
    )
    (project_dir / "改写目标.md").write_text(
        f"""# 改写目标

## 用户的意难平

- 待填写

## 切入节点

- {args.branch_point}

## 必须保留的原作事实

- 待填写

## 允许改变的事件

- 待填写

## 偏好与禁忌

- 偏好角色或 CP：
- 期待方向：
- 避免内容：
""",
        encoding="utf-8",
    )
    (project_dir / "创作日志.md").write_text(
        f"# 创作日志\n\n- {created_at}：创建项目，根节点 `{root_id}`。\n",
        encoding="utf-8",
    )
    print(f"已创建项目：{project_dir}")
    print(f"当前节点：{root_id}")


def command_add_node(args: argparse.Namespace) -> None:
    project_dir = Path(args.project_dir).expanduser().resolve()
    project, tree = load_project(project_dir)
    nodes = tree.get("nodes", {})
    if args.parent not in nodes:
        raise ValueError(f"父节点不存在：{args.parent}")
    parent = nodes[args.parent]
    if parent.get("ending"):
        raise ValueError("结局节点不能直接添加子节点；请先回溯到非结局节点")

    patch = parse_json_argument(args.state_patch, "state-patch")
    if not isinstance(patch, dict):
        raise ValueError("state-patch 顶层必须是 JSON 对象")
    options = parse_json_argument(args.options, "options")
    if not isinstance(options, list):
        raise ValueError("options 必须是 JSON 数组")
    if not args.ending and len(options) != 3:
        raise ValueError("非结局节点必须保存恰好 3 个选项")
    if args.ending and options:
        raise ValueError("结局节点的 options 应为空数组")
    if not args.ending:
        required_option_fields = {"label", "action", "cost", "opens"}
        labels: list[str] = []
        for index, option in enumerate(options, start=1):
            if not isinstance(option, dict):
                raise ValueError(f"第 {index} 个选项必须是 JSON 对象")
            missing = required_option_fields - option.keys()
            if missing:
                raise ValueError(
                    f"第 {index} 个选项缺少字段："
                    + ", ".join(sorted(missing))
                )
            labels.append(str(option["label"]))
        if len(set(labels)) != 3:
            raise ValueError("三个选项的 label 必须互不相同")

    number = project.get("next_node_number")
    if not isinstance(number, int) or number < 1:
        raise ValueError("project.json 的 next_node_number 无效")
    node_id = f"n{number:04d}"
    if node_id in nodes:
        raise ValueError(f"节点 ID 冲突：{node_id}")

    scene_path = (project_dir / args.scene).resolve()
    try:
        scene_path.relative_to(project_dir)
    except ValueError as exc:
        raise ValueError("scene 必须位于项目目录内") from exc
    if not scene_path.is_file():
        raise ValueError(f"场景文件不存在：{scene_path}")

    state = merge_patch(parent.get("state_snapshot", {}), patch)
    created_at = now_utc()
    node = {
        "id": node_id,
        "parent_id": args.parent,
        "children": [],
        "choice": args.choice,
        "title": args.title,
        "scene_file": str(scene_path.relative_to(project_dir)),
        "summary": args.summary,
        "state_snapshot": state,
        "options": options,
        "ending": bool(args.ending),
        "created_at": created_at,
    }
    nodes[node_id] = node
    parent.setdefault("children", []).append(node_id)
    project["current_node_id"] = node_id
    project["next_node_number"] = number + 1
    project["updated_at"] = created_at
    write_json(project_dir / "branch-tree.json", tree)
    write_json(project_dir / "project.json", project)
    render_state(project_dir, node_id, state)
    with (project_dir / "创作日志.md").open("a", encoding="utf-8") as handle:
        handle.write(f"- {created_at}：从 `{args.parent}` 创建 `{node_id}`：{args.title}。\n")
    print(f"已创建节点：{node_id}")


def command_checkout(args: argparse.Namespace) -> None:
    project_dir = Path(args.project_dir).expanduser().resolve()
    project, tree = load_project(project_dir)
    node = tree.get("nodes", {}).get(args.node)
    if node is None:
        raise ValueError(f"节点不存在：{args.node}")
    project["current_node_id"] = args.node
    project["updated_at"] = now_utc()
    write_json(project_dir / "project.json", project)
    render_state(project_dir, args.node, node.get("state_snapshot", {}))
    with (project_dir / "创作日志.md").open("a", encoding="utf-8") as handle:
        handle.write(f"- {project['updated_at']}：回溯并切换到 `{args.node}`。\n")
    print(f"已切换到节点：{args.node} {node.get('title', '')}")


def command_list(args: argparse.Namespace) -> None:
    project_dir = Path(args.project_dir).expanduser().resolve()
    project, tree = load_project(project_dir)
    nodes = tree.get("nodes", {})
    current = project.get("current_node_id")

    def walk(node_id: str, prefix: str = "", is_last: bool | None = None) -> None:
        node = nodes[node_id]
        marker = "*" if node_id == current else " "
        ending = " [结局]" if node.get("ending") else ""
        connector = "" if is_last is None else ("└─ " if is_last else "├─ ")
        print(f"{marker} {prefix}{connector}{node_id} {node.get('title', '')}{ending}")
        children = node.get("children", [])
        child_prefix = prefix
        if is_last is not None:
            child_prefix += "   " if is_last else "│  "
        for index, child_id in enumerate(children):
            walk(child_id, child_prefix, index == len(children) - 1)

    walk(tree["root_node_id"])


def validate_project(project_dir: Path) -> list[str]:
    errors: list[str] = []
    required = [
        "project.json",
        "原作基线.md",
        "改写目标.md",
        "branch-tree.json",
        "世界线状态.md",
        "创作日志.md",
        "剧情",
    ]
    for name in required:
        if not (project_dir / name).exists():
            errors.append(f"缺少：{name}")
    if errors:
        return errors
    try:
        project, tree = load_project(project_dir)
    except ValueError as exc:
        return [str(exc)]
    if project.get("schema_version") != SCHEMA_VERSION:
        errors.append("project.json schema_version 不受支持")
    if tree.get("schema_version") != SCHEMA_VERSION:
        errors.append("branch-tree.json schema_version 不受支持")
    nodes = tree.get("nodes")
    if not isinstance(nodes, dict) or not nodes:
        return errors + ["branch-tree.json nodes 必须是非空对象"]
    root_id = tree.get("root_node_id")
    if root_id not in nodes:
        errors.append("根节点不存在")
    current_id = project.get("current_node_id")
    if current_id not in nodes:
        errors.append("当前节点不存在")

    seen_children: set[str] = set()
    for node_id, node in nodes.items():
        if node.get("id") != node_id:
            errors.append(f"{node_id} 的 id 字段不一致")
        if not NODE_RE.match(node_id):
            errors.append(f"节点 ID 格式无效：{node_id}")
        parent_id = node.get("parent_id")
        if node_id == root_id:
            if parent_id is not None:
                errors.append("根节点 parent_id 必须为 null")
        elif parent_id not in nodes:
            errors.append(f"{node_id} 的父节点不存在：{parent_id}")
        elif node_id not in nodes[parent_id].get("children", []):
            errors.append(f"{node_id} 未出现在父节点 children 中")
        children = node.get("children", [])
        if not isinstance(children, list):
            errors.append(f"{node_id} 的 children 必须是数组")
            continue
        for child_id in children:
            if child_id not in nodes:
                errors.append(f"{node_id} 引用了不存在的子节点：{child_id}")
            if child_id in seen_children:
                errors.append(f"子节点被多个父节点引用：{child_id}")
            seen_children.add(child_id)
        if not isinstance(node.get("state_snapshot"), dict):
            errors.append(f"{node_id} 缺少有效状态快照")
        options = node.get("options")
        if not isinstance(options, list):
            errors.append(f"{node_id} 的 options 必须是数组")
        elif node.get("ending") and options:
            errors.append(f"结局节点 {node_id} 不应包含选项")
        elif node_id != root_id and not node.get("ending") and len(options) != 3:
            errors.append(f"非结局节点 {node_id} 必须包含 3 个选项")
        elif not node.get("ending"):
            required_option_fields = {"label", "action", "cost", "opens"}
            for index, option in enumerate(options, start=1):
                if not isinstance(option, dict):
                    errors.append(f"{node_id} 的第 {index} 个选项必须是对象")
                    continue
                missing = required_option_fields - option.keys()
                if missing:
                    errors.append(
                        f"{node_id} 的第 {index} 个选项缺少："
                        + ", ".join(sorted(missing))
                    )
        scene_file = node.get("scene_file")
        if node_id != root_id:
            if not scene_file:
                errors.append(f"{node_id} 缺少场景文件")
            elif not (project_dir / scene_file).is_file():
                errors.append(f"{node_id} 的场景文件不存在：{scene_file}")

    for node_id in nodes:
        visited: set[str] = set()
        cursor: str | None = node_id
        while cursor is not None:
            if cursor in visited:
                errors.append(f"检测到循环引用：{node_id}")
                break
            visited.add(cursor)
            cursor = nodes.get(cursor, {}).get("parent_id")
    return errors


def command_validate(args: argparse.Namespace) -> None:
    project_dir = Path(args.project_dir).expanduser().resolve()
    errors = validate_project(project_dir)
    if errors:
        print("项目验证失败：")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)
    project, tree = load_project(project_dir)
    print(
        f"项目有效：{len(tree['nodes'])} 个节点，"
        f"当前节点 {project['current_node_id']}"
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="创建同人分支项目")
    init_parser.add_argument("project_dir")
    init_parser.add_argument("--source-title", required=True)
    init_parser.add_argument("--input-mode", choices=["title", "upload"], required=True)
    init_parser.add_argument("--source-file", action="append", default=[])
    init_parser.add_argument("--branch-point", required=True)
    init_parser.add_argument("--perspective", default="第三人称")
    init_parser.add_argument("--scene-min", type=int, default=800)
    init_parser.add_argument("--scene-max", type=int, default=1500)
    init_parser.set_defaults(func=command_init)

    add_parser = subparsers.add_parser("add-node", help="从父节点创建新节点")
    add_parser.add_argument("project_dir")
    add_parser.add_argument("--parent", required=True)
    add_parser.add_argument("--choice", required=True)
    add_parser.add_argument("--title", required=True)
    add_parser.add_argument("--scene", required=True)
    add_parser.add_argument("--summary", required=True)
    add_parser.add_argument("--state-patch", required=True)
    add_parser.add_argument("--options", required=True)
    add_parser.add_argument("--ending", action="store_true")
    add_parser.set_defaults(func=command_add_node)

    checkout_parser = subparsers.add_parser("checkout", help="切换当前世界线节点")
    checkout_parser.add_argument("project_dir")
    checkout_parser.add_argument("--node", required=True)
    checkout_parser.set_defaults(func=command_checkout)

    list_parser = subparsers.add_parser("list", help="显示分支树")
    list_parser.add_argument("project_dir")
    list_parser.set_defaults(func=command_list)

    validate_parser = subparsers.add_parser("validate", help="验证项目结构")
    validate_parser.add_argument("project_dir")
    validate_parser.set_defaults(func=command_validate)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if getattr(args, "scene_min", 1) < 1:
        parser.error("scene-min 必须大于 0")
    if getattr(args, "scene_max", 1) < getattr(args, "scene_min", 1):
        parser.error("scene-max 必须大于或等于 scene-min")
    try:
        args.func(args)
    except (OSError, ValueError) as exc:
        print(f"错误：{exc}", file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
