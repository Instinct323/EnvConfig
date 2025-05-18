#!/bin/bash

# conda create -n tongzj python=3.10.16 -y
pip install -r pymod/requirements.txt && \
pip install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 --index-url https://download.pytorch.org/whl/cu124 && \
pip install -r ModelsAPI/requirements.txt
