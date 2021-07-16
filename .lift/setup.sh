#!/usr/bin/env bash
apt-get update &&     \
apt-get install --no-install-recommends -y     \
python3.8 python3-pip python3.8-dev

pip install detect-secrets