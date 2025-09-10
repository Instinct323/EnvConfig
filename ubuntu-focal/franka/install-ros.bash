#!/bin/bash
# ./install-ros.bash ~/catkin_ws

if [ $(id -u) -eq 0 ]; then

  # https://www.franka.cn/FCI/installation_linux.html#building-from-source
  cd $1
  git clone -b $ROS_DISTRO-devel --recursive https://github.com/frankaemika/franka_ros src/franka_ros

  apt install ros-noetic-boost-sml ros-noetic-combined-robot-hw ros-noetic-joint-trajectory-controller
  apt install ros-noetic-moveit ros-noetic-panda-moveit-config

  rosdep install --from-paths src --ignore-src --rosdistro $ROS_DISTRO -y --skip-keys libfranka
  catkin_make -DCMAKE_BUILD_TYPE=Release -DFranka_DIR:PATH=/opt/libfranka

else
  echo "error: permission denied."
fi
