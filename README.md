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

- `~/.bashrc`
  - ADD: export LANG=en_US
  - ADD: export LANGUAGE=en_US

- `/etc/apt/sources.list`
  - [https://developer.aliyun.com/mirror/ubuntu](https://developer.aliyun.com/mirror/ubuntu)

- `/etc/default/grub`
  - MOD: GRUB_DEFAULT=1>4
  - MOD: GRUB_TIMEOUT_STYLE=menu
  - MOD: GRUB_TIMEOUT=10
  - RUN: update-grub

- `/etc/fstab`
  - RUN: ntfsfix /dev/*
  - ADD: /dev/disk/by-uuid/* /media/user/* ntfs defaults 0 2

- `/etc/ppp/options`
  - DEL: lcp-echo-interval
  - DEL: lcp-echo-failure

- `/etc/ssh/sshd_config`
  - PasswordAuthentication yes
  - PermitEmptyPasswords no
  - sudo service ssh start

- `ln -s {src} {dst}`
  - ~/.cache
  - ~/Downloads
  - ~/miniconda3
  - ~/Zotero

# Windows

- MOD env: Download, Documents, tmp
- MOD time-sync: ntp.aliyun.com
- MOD virtual-memory:  0.125 ~ 3 RAM
- MOD power: Dormancy