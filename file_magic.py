from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time

class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        
        #new_name = "new_file_" + str(self.i) + ".txt" #### change according to file type and name wanted ##############

        for filename in os.listdir(folder_to_track):
            
            print("Moved to " + folder_destination)

        
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)

folder_to_track = "/Users/tekreplay/Desktop/f1"
folder_destination = "/Users/tekreplay/Desktop/f2"
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