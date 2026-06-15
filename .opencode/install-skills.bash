#!/bin/bash

[ -z "$1" ] && { echo "Error: missing target dir"; exit 1; }
[ ! -d "$1" ] && { echo "Error: '$1' does not exist"; exit 1; }

# local
cp -r skills "$1"

# git
cd /tmp
# anthropics
git clone https://github.com/anthropics/skills.git
rm -rf skills/skills/pdf
cp -r skills/skills "$1"
rm -rf skills
# andrej-karpathy-skills
git clone https://github.com/forrestchang/andrej-karpathy-skills.git
cp -r andrej-karpathy-skills/skills "$1"
rm -rf andrej-karpathy-skills

# clawhub: https://clawhub.ai/
cd "$1"
bun i -g clawhub
clawhub install --force caveman
clawhub install --force github
clawhub install --force mineru-ai
clawhub install --force multi-search-engine

# other
bun i -g @colbymchenry/codegraph
codegraph install --yes