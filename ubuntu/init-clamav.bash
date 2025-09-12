#!/bin/bash

if ! [ $(id -u) -eq 0 ]; then
  echo "error: permission denied."
  exit 1
fi

apt install -y clamav clamav-daemon
/etc/init.d/clamav-freshclam stop
freshclam
/etc/init.d/clamav-freshclam start
# clamscan -r /
