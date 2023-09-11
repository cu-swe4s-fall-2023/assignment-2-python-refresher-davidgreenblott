#!/bin/bash

set -e # stop on error
set -u # raise error if variable is unset
set -o pipefail #fail if any prior step failed
chmod +x run.sh
echo "Running print_fires.py"
python print_fires.py

