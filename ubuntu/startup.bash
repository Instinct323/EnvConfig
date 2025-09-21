#!/bin/bash

gnome-terminal \
  --tab --title="NviTop" -e "bash -c 'nvitop; exec bash'" \
  --tab --title="Zotero" -e "bash -c '/opt/Zotero/zotero; exec bash'" \

if [ "$ROS_VERSION" = "1" ]; then
  gnome-terminal --tab --title="ROS core" -e "bash -c 'roscore; exec bash'"
fi
