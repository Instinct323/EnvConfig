#!/bin/bash
set -euo pipefail

[ -z "${1:-}" ] && { echo "Error: missing target dir"; exit 1; }
[ ! -d "$1" ] && { echo "Error: '$1' does not exist"; exit 1; }

SRC="$(cd "$(dirname "$0")" && pwd)"
DST="$1"

# local
cp -r "${SRC}/skills" "$DST"
cp "${SRC}/AGENTS.md" "$DST"

# git
TMPDIR=$(mktemp -d)
trap 'rm -rf "$TMPDIR"' EXIT
cd "$TMPDIR"

## anthropics
git clone --depth 1 https://github.com/anthropics/skills.git
rm -rf skills/skills/pdf
cp -r skills/skills "$DST"

## andrej-karpathy-skills
git clone --depth 1 https://github.com/forrestchang/andrej-karpathy-skills.git
cp -r andrej-karpathy-skills/skills "$DST"

# clawhub: https://clawhub.ai/
cd "$DST"
bun i -g clawhub
clawhub install --force @skaravind/caveman
clawhub install --force @mineru-extract/mineru-ai
clawhub install --force @gpyangyoujun/multi-search-engine
