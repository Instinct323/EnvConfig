#!/bin/bash
set -euo pipefail

SRC="$(cd "$(dirname "$0")" && pwd)"
DST=~/.config/opencode

"${SRC}/install-skills.bash" "$DST"

# codegraph
bun i -g @colbymchenry/codegraph
codegraph install --yes
