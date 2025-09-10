#!/bin/bash

# https://wiki.ros.org/noetic/Installation/Ubuntu
echo "deb http://packages.ros.org/ros/ubuntu focal main" > /etc/apt/sources.list.d/ros-latest.list
cat /tmp/ros.asc | apt-key add -

# Python 3 Libraries: /opt/ros/noetic/lib/python3/dist-packages
apt update
apt upgrade -y
apt install -y ros-noetic-desktop-full
apt install python3-rosdep ros-noetic-ros-numpy
