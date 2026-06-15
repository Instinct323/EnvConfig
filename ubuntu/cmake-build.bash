#!/bin/bash
# cmake-build.bash <repo-path>

[ -z "$1" ] && { echo "Error: missing target dir"; exit 1; }
[ ! -d "$1" ] && { echo "Error: '$1' does not exist"; exit 1; }

cd "$1"
mkdir -p build && cd build && cmake .. && make
