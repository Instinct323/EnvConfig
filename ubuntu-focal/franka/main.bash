#!/bin/bash

roslaunch panda_moveit_config franka_control.launch \
    robot_ip:=172.16.0.2 load_gripper:=true robot:=panda
