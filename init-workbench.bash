#!/bin/bash

mkdir Workbench
cd Workbench
mkdir asssets
mkdir Lab

# export URL_BASE=https://github.com/Instinct323
export URL_BASE=git@github.com:Instinct323

git clone $URL_BASE/cppmod.git
git clone $URL_BASE/pymod.git
git clone $URL_BASE/ModelsAPI.git
git clone $URL_BASE/.git notes
git clone $URL_BASE/EnvConfig.git
