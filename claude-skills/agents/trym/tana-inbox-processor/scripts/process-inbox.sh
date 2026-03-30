#!/usr/bin/env bash
# Wrapper script for Clawdbot skill invocation
set -euo pipefail

TANA_SCRIPTS_DIR="$HOME/tana-scripts"

# Run the inbox processor
exec "$TANA_SCRIPTS_DIR/tana-inbox-processor.sh" "$@"
