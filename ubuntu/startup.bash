#!/bin/bash

gnome-terminal \
  --tab --title="NviTop" -e "bash -c 'nvitop; exec bash'" \
  --tab --title="ROS core" -e "bash -c 'roscore; exec bash'" \
  --tab --title="Zotero" -e "bash -c '/opt/Zotero/zotero; exec bash'" \
