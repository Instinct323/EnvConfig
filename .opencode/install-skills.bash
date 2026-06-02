#!/bin/bash

export OC_CONFIG=~/.config/opencode/

# local
cp -r skills $OC_CONFIG

# git
cd /tmp

# anthropics
git clone https://github.com/anthropics/skills.git
rm -rf skills/skills/pdf
cp -r skills/skills $OC_CONFIG
rm -rf skills

# andrej-karpathy-skills
git clone https://github.com/forrestchang/andrej-karpathy-skills.git
cp -r andrej-karpathy-skills/skills $OC_CONFIG
rm -rf andrej-karpathy-skills

# clawhub: https://clawhub.ai/
cd $OC_CONFIG
bun i -g clawhub
bunx clawhub install --force github
bunx clawhub install --force mineru-ai
bunx clawhub install --force multi-search-engine
