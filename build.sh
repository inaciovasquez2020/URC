#!/bin/sh
set -eu

python3 urc_node.py
shasum -a 256 genesis.json > genesis.json.sha256
shasum -a 256 -c genesis.json.sha256
echo "OK: reproducible genesis"
