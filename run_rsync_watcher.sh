#!/bin/bash
cd "$(dirname "$0")"
source venv/bin/activate
python rsync_watcher.py "$@"