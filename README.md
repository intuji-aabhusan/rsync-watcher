# RSync Watcher

A simple Python utility that monitors a directory for changes and automatically syncs them to a remote server using rsync.

## Overview

RSync Watcher uses the `watchdog` library to detect file system changes in real-time and triggers an rsync operation whenever changes are detected.

## Requirements

- Python 3.6+
- rsync on both local and remote hosts

## Installation

1. Create and activate a virtual environment:

```bash
python -m venv venv

source venv/bin/activate
```

2. Install the required packages using requirements.txt:

```bash
pip install -r requirements.txt
```

## Usage

Run the script with the directory to monitor and the remote location:

```bash
python rsync_watcher.py [directory_path] --remote user@host:/path/to/destination
```

### Arguments

- `directory_path`: Path to the directory to monitor (optional, defaults to current directory)
- `--remote` or `-r`: Remote location in the format `user@host:/path/to/destination` (required)

### Create Alias

You can also create an alias to run the application easily. Update your `.bashrc` or equivalent file and add the following line:

```
alias rsync_watcher='/path/to/your/directory/run_rsync_watcher.sh'
```

Make sure that the `run_rsync_watcher.sh` is executable.

```bash
chmod +x run_rsync_watcher.sh
```

Then, you can simply run:

```bash
rsync_watcher [directory_path] --remote user@host:/path/to/destination
```

## Notes

- The script uses `rsync -avz --delete` options, which:
  - `-a`: Archive mode (preserves permissions, timestamps, etc.)
  - `-v`: Verbose output
  - `-z`: Compress data during transfer
  - `--delete`: Delete files on the receiving side that don't exist on the sending side
- The debounce mechanism is set to 2 seconds by default
