#!/bin/bash

export TMP=/tmp/repo
export BIN=/usr/local/bin

git clone https://github.com/Instinct323/EnvConfig.git $TMP

# Copy specific scripts
cp $TMP/ubuntu/* $TMP
cp $TMP/ubuntu-$(lsb_release -cs)/* $TMP

# Copy all scripts
cp $TMP/*.bashrc ~
cp $TMP/*.bash $BIN/

# Enable scripts
chmod +x $BIN/*.bash

# Summary
rm -rf $TMP
ls $BIN
