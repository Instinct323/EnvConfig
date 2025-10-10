#!/bin/bash
# init-disk.bash <disk-path>
cd $1

export USER=Instinct323
# export URL_BASE=https://github.com/$USER
export URL_BASE=git@github.com:$USER

# --- Downloads ---
mkdir Downloads

# --- Information ---
mkdir Information
git clone $URL_BASE/$USER.git Information/notes

# --- Workbench ---
mkdir Workbench
cd Workbench

mkdir 3rd-party
mkdir asssets
mkdir Lab

git clone $URL_BASE/cppmod.git
git clone $URL_BASE/pymod.git
git clone $URL_BASE/EnvConfig.git
git clone $URL_BASE/ModelsAPI.git
git clone $URL_BASE/ROS-dev-space.git
