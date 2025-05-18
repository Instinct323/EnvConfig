#!/bin/bash

export TMP=/tmp/repo
export BIN=/usr/local/bin

git clone https://github.com/Instinct323/EnvConfig.git $TMP
cp $TMP/ubuntu/* $TMP
cp $TMP/ubuntu-$(lsb_release -cs)/* $TMP

cp $TMP/*.bashrc ~
cp $TMP/*.bash $BIN/

chmod +x $BIN/*.bash
rm -rf $TMP

# sed -i "s/\r$//" bin/*
ls $BIN
