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
            #Move files based on extention
            # Documents
            if file.suffix == '.txt':
                print('file is .txt file!')
                shutil.move(src, "/Users/michaelwilliams/Desktop/michaelwilliams/documents")
            elif file.suffix == '.docx':
                print('file is an docx file!')
                shutil.move(src, "/Users/michaelwilliams/Desktop/michaelwilliams/documents")
            elif file.suffix == '.pdf':
                print('file is an pdf file!')
                shutil.move(src, "/Users/michaelwilliams/Desktop/michaelwilliams/documents")
            # Spreadsheets
            elif file.suffix == '.xls':
                print('file is a spreadsheet!')
                shutil.move(src, "/Users/michaelwilliams/Desktop/mw/spreadsheets")
            elif file.suffix == '.xlsx':
                print('file is a spreadsheet!')
                shutil.move(src, "/Users/michaelwilliams/Desktop/mw/spreadsheets")
            elif file.suffix == '.csv':
                print('file is a spreadsheet!')
                shutil.move(src, "/Users/michaelwilliams/Desktop/mw/spreadsheets")

            # Images
            elif file.suffix == '.png':
                print('file is an image!')
                shutil.move(src, "/Users/michaelwilliams/Desktop/mw/images")
            elif file.suffix == '.jpg':
                print('file is an image!')
                shutil.move(src, "/Users/michaelwilliams/Desktop/mw/images")
            elif file.suffix == '.jpeg':
                print('file is an image!')
                shutil.move(src, "/Users/michaelwilliams/Desktop/mw/images")
            # Movies
            elif file.suffix == '.mp4':
                print('file is an movie!')
                shutil.move(src, "/Users/michaelwilliams/Desktop/mw/movies")


            # Packages
            elif file.suffix == '.dmg':
                print('file is an installation package!')
                shutil.move(src, "/Users/michaelwilliams/Desktop/mw/packages")
            elif file.suffix == '.zip':
                print('file is an compressed folder!')
                shutil.move(src, "/Users/michaelwilliams/Desktop/mw/packages")
    
            # if filetype is unknown, it will default to the 'others' directory
            else:
                print('filetype currently unknown')
                shutil.move(src, "/Users/michaelwilliams/Desktop/mw/others")



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