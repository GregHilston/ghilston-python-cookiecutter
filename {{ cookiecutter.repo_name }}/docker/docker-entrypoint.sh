#!/bin/bash
# bash "strict mode"
set -euo pipefail
IFS=$'\n\t'

# activate our virtual environment here
. /opt/pysetup/.venv/bin/activate

# You can put other setup logic here
# adds poetry binary to path
PATH=$PATH:$HOME/.poetry/bin

# Evaluating passed command:
exec "$@"
