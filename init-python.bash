#!/bin/bash

# conda create -n tongzj python=3.10.16 -y
pip install -r pymod/requirements.txt && \
pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cu124 && \
pip install -r ModelsAPI/requirements.txt
