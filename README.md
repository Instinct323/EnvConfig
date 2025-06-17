# General

```bash
# Initialize git configuration
python new-user.py user-tongzj.json
```

# Ubuntu

```bash
# Install utils
ubuntu/init-ubuntu.bash
# Clone scripts
ubuntu/clone-bin.bash
# TODO: Copy fonts
```

- /etc/fstab
  - RUN: ntfsfix /dev/*
  - ADD: /dev/disk/by-uuid/* /media/user/* ntfs defaults 0 2

- ~/.bashrc
  - ADD: export LANG=en_US
  - ADD: export LANGUAGE=en_US
  - ADD: export PATH=$PATH:~/.local/bin

- /etc/default/grub
  - MOD: GRUB_DEFAULT=2
  - RUN: update-grub

- /etc/ppp/options
  - DEL: lcp-echo-interval
  - DEL: lcp-echo-failure

- /etc/apt/sources.list
  - [https://developer.aliyun.com/mirror/ubuntu](https://developer.aliyun.com/mirror/ubuntu)

# Windows

- MOD env: Download, Documents, tmp
- MOD time-sync: ntp.aliyun.com
- MOD virtual-memory:  0.125 ~ 3 RAM
- MOD power: Dormancy