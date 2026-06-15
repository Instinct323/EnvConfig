#!/bin/bash
# cmake-install.bash <repo-path>

if ! [ $(id -u) -eq 0 ]; then
  echo "error: permission denied."
  exit 1
fi

# main
cmake-build.bash "$1"

cd "$1/build"
make install
