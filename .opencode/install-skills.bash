#!/bin/bash

[ -z "$1" ] && { echo "Error: missing target dir"; exit 1; }
[ ! -d "$1" ] && { echo "Error: '$1' does not exist"; exit 1; }

# local
cp -r ${0%/*}/skills "$1"

# git
cd /tmp
## anthropics
git clone https://github.com/anthropics/skills.git
rm -rf skills/skills/pdf
cp -r skills/skills "$1"
rm -rf skills
## andrej-karpathy-skills
git clone https://github.com/forrestchang/andrej-karpathy-skills.git
cp -r andrej-karpathy-skills/skills "$1"
rm -rf andrej-karpathy-skills

# clawhub: https://clawhub.ai/
cd "$1"
bun i -g clawhub
clawhub install --force @skaravind/caveman
clawhub install --force @mineru-extract/mineru-ai
clawhub install --force @gpyangyoujun/multi-search-engine
