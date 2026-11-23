#!/bin/bash

# https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html

# Python 3.10 Libraries: /opt/ros/humble/lib/python3.10/site-packages

curl -fsSL https://raw.githubusercontent.com/Instinct323/EnvConfig/master/ubuntu/ros/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu jammy main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null
apt update
apt install -y libegl-mesa0 ros-humble-desktop python3-colcon-common-extensions
