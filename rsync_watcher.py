import time
import sys
import argparse
import subprocess
import os
from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

class MyEventHandler(FileSystemEventHandler):
    def __init__(self, source_directory, remote_location):
        self.source_directory = source_directory
        self.remote_location = remote_location
        self.last_synced_time = time.time()
        self.min_sync_interval = 2  # seconds, for debounce
        
    def on_any_event(self, event: FileSystemEvent) -> None:         
        # Debounce
        current_time = time.time()
        if current_time - self.last_synced_time < self.min_sync_interval:
            return
            
        self.last_synced_time = current_time
        
        try:
            print(f"Change detected: {event.src_path}")
            print(f"Syncing {self.source_directory} to {self.remote_location}...")
            
           
            rsync_cmd = [
                "rsync",
                "-avz",  # archive mode, verbose, compress
                "--delete", 
                f"{self.source_directory}",
                self.remote_location 
            ]
            
            result = subprocess.run(rsync_cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                print("Sync completed successfully")
            else:
                print(f"Sync failed: {result.stderr}")
                
        except Exception as e:
            print(f"Error during sync: {e}")

def main():
    parser = argparse.ArgumentParser(description='Monitor a directory and sync changes with rsync')
    parser.add_argument('path', type=str, nargs='?', default='.',
                        help='Path to the directory to monitor (default: current directory)')
    parser.add_argument('--remote', '-r', type=str, required=True,
                        help='Remote location in the format user@host:/path/to/destination')
    args = parser.parse_args()
    
    directory_path = args.path
    remote_location = args.remote
    
    print(f"Monitoring directory: {directory_path}")
    print(f"Remote destination: {remote_location}")
    
    event_handler = MyEventHandler(directory_path, remote_location)
    observer = Observer()
    observer.schedule(event_handler, directory_path, recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Monitoring stopped.")
    finally:
        observer.stop()
        observer.join()

if __name__ == "__main__":
    main()