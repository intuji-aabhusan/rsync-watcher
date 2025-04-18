#!/bin/bash

script_dir="$(dirname "$0")"
source "${script_dir}/venv/bin/activate"
python "${script_dir}/rsync_watcher.py" "$@"