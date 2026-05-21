#!/usr/bin/env zsh
set -e

SOURCE_DIR="/Users/linzifeng/Documents/产策AI工作流/codex-skills/product-info-house"
TARGET_DIR="/Users/linzifeng/.codex/skills/product-info-house"

mkdir -p "$TARGET_DIR"
cp -R "$SOURCE_DIR/." "$TARGET_DIR/"

echo "product-info-house skill 已安装到：$TARGET_DIR"
