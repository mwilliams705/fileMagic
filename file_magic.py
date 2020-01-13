from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time
import shutil
from pathlib import Path

class MyHandler(FileSystemEventHandler):
    
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            
            
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            file = Path(filename)
            #Move files based on extention

            if file.suffix == '.txt':
                print('file is .txt!')
                shutil.move(src, "/Users/michaelwilliams/Desktop/michaelwilliams/documents")
            elif file.suffix == '.docx':
                print('file is an image!')
                shutil.move(src, "/Users/michaelwilliams/Desktop/michaelwilliams/documents")

            # Images
            elif file.suffix == '.png':
                print('file is an image!')
                shutil.move(src, "/Users/michaelwilliams/Desktop/michaelwilliams/images")
            elif file.suffix == '.jpg':
                print('file is an image!')
                shutil.move(src, "/Users/michaelwilliams/Desktop/michaelwilliams/images")
            elif file.suffix == '.jpeg':
                print('file is an image!')
                shutil.move(src, "/Users/michaelwilliams/Desktop/michaelwilliams/images")


            # Packages
            elif file.suffix == '.dmg':
                print('file is an installation package!')
                shutil.move(src, "/Users/michaelwilliams/Desktop/michaelwilliams/packages")
            elif file.suffix == '.zip':
                print('file is an compressed folder!')
                shutil.move(src, "/Users/michaelwilliams/Desktop/michaelwilliams/packages")



folder_to_track = "/Users/michaelwilliams/Downloads"
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