#!/bin/bash

gnome-terminal \
  --tab --title="ROS core" -e "bash -c 'roscore; exec bash'" \
  --tab --title="Zotero" -e "bash -c 'zotero; exec bash'" \
  --tab --title="NviTop" -e "bash -c 'nvitop; exec bash'"
