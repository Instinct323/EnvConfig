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

# clawhub: https://clawhub.ai/
cd $OC_CONFIG
npm i -g clawhub
clawhub install mineru-ai   # https://clawhub.ai/mineru-extract/mineru-ai
