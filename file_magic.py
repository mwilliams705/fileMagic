from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time
import shutil
import getpass
from pathlib import Path

class MyHandler(FileSystemEventHandler):
    
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            
            
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            file = Path(filename)


folder_to_track = "/Users/michaelwilliams/Desktop/mw"
folder_destination = "/Users/michaelwilliams/Desktop/f2"
  


event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()