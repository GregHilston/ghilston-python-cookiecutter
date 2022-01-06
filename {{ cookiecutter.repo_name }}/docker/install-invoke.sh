#!/bin/bash
# bash "strict mode"
set -euo pipefail
IFS=$'\n\t

# Installs Pyinvoke
# This can be used by Docker Compose to add Pyinvoke which is not generally available to the Docker image that we've
# created.
pip install invoke