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

_For Linux environments (including WSL). For usage in Windows, please refer to additional steps below._

Run the script with the directory to monitor and the remote location:

```bash
python rsync_watcher.py [directory_path] --remote user@host:/path/to/destination
```

### Arguments

- `directory_path`: Path to the directory to monitor (optional, defaults to current directory)
- `--remote` or `-r`: Remote location in the format `user@host:/path/to/destination` (required)

## Additional Steps for Windows

Since rsync doesn't natively ship with Windows, we'll have to install it manually. We'll use Cygwin for this.

1. Download and install [Cygwin](https://www.cygwin.com/). Make sure to tick rsync and ssh while installing.
2. Add Cygwin to path. (C:\cygwin64\bin)
3. Run the script

```
python rsync_watcher.py [directory_path] --remote user@host:/path/to/destination -e [cygwin_ssh_path]
```

`cygwin_ssh_path`: `C:\cygwin64\bin\ssh.exe`
`directory_path`: Should be an absolute path starting from drive prefix. Example `C:\source_directory\` and should contain no spaces in between.

## Notes

- The script uses `rsync -avz --delete` options, which:
  - `-a`: Archive mode (preserves permissions, timestamps, etc.)
  - `-v`: Verbose output
  - `-z`: Compress data during transfer
  - `--delete`: Delete files on the receiving side that don't exist on the sending side
- The debounce mechanism is set to 2 seconds by default
