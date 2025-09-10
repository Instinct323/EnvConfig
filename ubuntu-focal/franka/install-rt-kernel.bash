#!/bin/bash

export RTK=/opt/rt-kernel

if [ $(id -u) -eq 0 ]; then

  # https://www.franka.cn/FCI/installation_linux.html#setting-up-the-real-time-kernel
  apt install -y zstd
  apt install -y build-essential bc curl debhelper dpkg-dev devscripts fakeroot libssl-dev libelf-dev bison flex cpio kmod rsync libncurses-dev
  
  mkdir -p $RTK && cd $RTK
  
  curl -LO https://www.kernel.org/pub/linux/kernel/v5.x/linux-5.9.1.tar.xz
  curl -LO https://www.kernel.org/pub/linux/kernel/v5.x/linux-5.9.1.tar.sign
  curl -LO https://www.kernel.org/pub/linux/kernel/projects/rt/5.9/patch-5.9.1-rt20.patch.xz
  curl -LO https://www.kernel.org/pub/linux/kernel/projects/rt/5.9/patch-5.9.1-rt20.patch.sign
  xz -d *.xz
  
  tar xf linux-*.tar
  cd linux-*/
  patch -p1 < ../patch-*.patch
  
  cp -v /boot/config-$(uname -r) .config
  
  scripts/config --disable DEBUG_INFO
  scripts/config --disable DEBUG_INFO_DWARF_TOOLCHAIN_DEFAULT
  scripts/config --disable DEBUG_KERNEL
  scripts/config --disable SYSTEM_TRUSTED_KEYS
  scripts/config --disable SYSTEM_REVOCATION_LIST
  scripts/config --disable PREEMPT_NONE
  scripts/config --disable PREEMPT_VOLUNTARY
  scripts/config --disable PREEMPT
  scripts/config --enable PREEMPT_RT
  
  make olddefconfig
  make -j$(nproc) deb-pkg
  IGNORE_PREEMPT_RT_PRESENCE=1 dpkg -i ../linux-headers-*.deb ../linux-image-*.deb

  # addgroup realtime
  # usermod -a -G realtime $(whoami)
  # gedit /etc/security/limits.conf

else
  echo "error: permission denied."
fi
