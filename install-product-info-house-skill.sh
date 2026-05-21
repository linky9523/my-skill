#!/usr/bin/env zsh
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SOURCE_DIR="$SCRIPT_DIR/codex-skills/product-info-house"
TARGET_DIR="/Users/linzifeng/.codex/skills/product-info-house"

mkdir -p "$TARGET_DIR"
cp -R "$SOURCE_DIR/." "$TARGET_DIR/"

echo "product-info-house skill 已安装到：$TARGET_DIR"
