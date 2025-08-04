#!/bin/bash

export LIBFRANKA=/opt/libfranka

if [ $(id -u) -eq 0 ]; then

  # https://github.com/frankarobotics/libfranka/blob/main/README.md
  apt update
  apt install -y build-essential cmake git libpoco-dev libeigen3-dev libfmt-dev

  apt install -y lsb-release curl
  mkdir -p /etc/apt/keyrings
  curl -fsSL http://robotpkg.openrobots.org/packages/debian/robotpkg.asc | tee /etc/apt/keyrings/robotpkg.asc
  echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/robotpkg.asc] http://robotpkg.openrobots.org/packages/debian/pub $(lsb_release -cs) robotpkg" | tee /etc/apt/sources.list.d/robotpkg.list

  apt update
  apt install -y robotpkg-pinocchio

  apt remove "*libfranka*"

  git clone --recurse-submodules https://github.com/frankaemika/libfranka.git $LIBFRANKA
  cd $LIBFRANKA
  git checkout 0.8.0
  git submodule update
  mkdir build && cd build

  cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_PREFIX_PATH=/opt/openrobots/lib/cmake -DBUILD_TESTS=OFF ..
  make
  cpack -G DEB
  dpkg -i libfranka*.deb

else
  echo "error: permission denied."
fi
