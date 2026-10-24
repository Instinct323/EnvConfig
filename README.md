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
  - ADD: alias occsta="ncdu / --exclude /mnt"
  - ADD (wsl): export LIBGL_ALWAYS_SOFTWARE=1

- `/etc/apt/sources.list`
  - [https://developer.aliyun.com/mirror/ubuntu](https://developer.aliyun.com/mirror/ubuntu)

- `/etc/default/grub`
  - MOD: GRUB_DEFAULT=1>4
  - MOD: GRUB_TIMEOUT_STYLE=menu
  - MOD: GRUB_TIMEOUT=10
  - RUN: update-grub

- `/etc/fstab`
  - RUN: ntfsfix /dev/{TARGET}
  - ADD: /dev/disk/by-uuid/{TARGET} /media/user/{DST} ntfs-3g defaults,uid=1000,gid=1000,umask=022 0 0

- `/etc/ppp/options`
  - DEL: lcp-echo-interval
  - DEL: lcp-echo-failure

- `/etc/ssh/sshd_config`
  - PasswordAuthentication yes
  - PermitEmptyPasswords no
  - sudo service ssh start

- `ln -s {src} {dst}`
  - ~/.cache
  - ~/miniconda3

# Windows

- MOD env: Download, Documents, tmp
- MOD time-sync: ntp.aliyun.com
- MOD virtual-memory:  0.125 ~ 3 RAM
- MOD power: Dormancy