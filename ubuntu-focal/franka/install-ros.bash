#!/bin/bash

# https://www.franka.cn/FCI/installation_linux.html#building-from-source
mkdir -p $1/src && cd $1

git clone --recursive https://github.com/frankaemika/franka_ros src/franka_ros
cd src/franka_ros
git checkout noetic-devel
cd ../..

rosdep install --from-paths src --ignore-src --rosdistro noetic -y --skip-keys libfranka
catkin_make -DCMAKE_BUILD_TYPE=Release -DFranka_DIR:PATH=/opt/libfranka
