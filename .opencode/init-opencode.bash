#!/bin/bash

${0%/*}/install-skills.bash ~/.config/opencode/

# codegraph
bun i -g @colbymchenry/codegraph
codegraph install --yes
