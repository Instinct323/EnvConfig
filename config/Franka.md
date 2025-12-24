# Ethernet

IPv4:
- 方式: 手动
- 地址: 172.16.0.100
- 子网掩码: 255.255.255.0

fci-ip: 172.16.0.2

# Requirements

通过以下命令查看 Ethernet 设备:

```bash
sudo lshw -class network
```

连接 Franka 线缆后，网卡协商速率需达到 1Gbps, 可通过以下命令检查网卡速率 (使用 `ip a` 查看网卡名称):

```bash
ethtool enp7s0
```

# launch

[DOC](https://www.franka.cn/FCI/franka_ros.html)

```bash
roslaunch panda_moveit_config franka_control.launch \
    robot_ip:=<fci-ip> load_gripper:=<true|false> robot:=<panda|fr3> \
    allow_trajectory_execution:=true octomap_frame:=camera_link
# TODO: https://github.com/moveit/panda_moveit_config/blob/a86da56ab1c756a851d8ee2a06dd04266d1653d6/launch/sensor_manager.launch.xml
```
