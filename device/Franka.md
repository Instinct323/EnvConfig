# Lab's Panda

IPv4:
- 方式: 手动
- 地址: 172.16.0.100
- 子网掩码: 255.255.255.0

fci-ip: 172.16.0.2

# launch

[DOC](https://www.franka.cn/FCI/franka_ros.html)

```bash
roslaunch panda_moveit_config franka_control.launch \
    robot_ip:=<fci-ip> load_gripper:=<true|false> robot:=<panda|fr3> \
    allow_trajectory_execution:=true octomap_frame:=camera_link
# TODO: https://github.com/moveit/panda_moveit_config/blob/a86da56ab1c756a851d8ee2a06dd04266d1653d6/launch/sensor_manager.launch.xml
```
