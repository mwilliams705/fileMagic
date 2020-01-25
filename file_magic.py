from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os 
import json
import shutil
import getpass
from datetime import datetime
from time import gmtime, strftime

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != username:
                # try:
                    new_name = filename
                    extension = 'noname'
                    try:
                        extension = str(os.path.splitext(folder_to_track + '/' + filename)[1])
                        path = extensions_folders[extension]
                    except Exception:
                        extension = 'noname'

                    now = datetime.now()
                    year = now.strftime("%Y")
                    month = now.strftime("%m")

                    folder_destination_path = extensions_folders[extension]
                    
                    year_exists = False
                    month_exists = False
                    
                    for folder_name in os.listdir(extensions_folders[extension]):
                        if folder_name == year:
                            folder_destination_path = extensions_folders[extension] + "/" +year
                            year_exists = True
                            for folder_month in os.listdir(folder_destination_path):
                                if month == folder_month:
                                    folder_destination_path = extensions_folders[extension] + "/" + year + "/" + month
                                    month_exists = True
                    if not year_exists:
                        os.mkdir(extensions_folders[extension] + "/" + year)
                        folder_destination_path = extensions_folders[extension] + "/" + year
                    if not month_exists:
                        os.mkdir(folder_destination_path + "/" + month)
                        folder_destination_path = folder_destination_path + "/" + month
                    


                    file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    while file_exists:
                        i += 1
                        new_name = os.path.splitext(folder_to_track + '/' + filename)[0] + str(i) + os.path.splitext(folder_to_track + '/' + filename)[1]
                        new_name = new_name.split("/")[4]
                        file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    src = folder_to_track + "/" + filename

                    new_name = folder_destination_path + "/" + new_name
                    os.rename(src, new_name)
                # except Exception:
                #     print(filename)
username = getpass.getuser()
extensions_folders = {
#No name
    'noname' : "/Users/"+username+"/Desktop/"+username+"/Other/Uncategorized",
#Audio
    '.aif' : "/Users/"+username+"/Desktop/"+username+"/Media/Audio",
    '.cda' : "/Users/"+username+"/Desktop/"+username+"/Media/Audio",
    '.mid' : "/Users/"+username+"/Desktop/"+username+"/Media/Audio",
    '.midi' : "/Users/"+username+"/Desktop/"+username+"/Media/Audio",
    '.mp3' : "/Users/"+username+"/Desktop/"+username+"/Media/Audio",
    '.mpa' : "/Users/"+username+"/Desktop/"+username+"/Media/Audio",
    '.ogg' : "/Users/"+username+"/Desktop/"+username+"/Media/Audio",
    '.wav' : "/Users/"+username+"/Desktop/"+username+"/Media/Audio",
    '.wma' : "/Users/"+username+"/Desktop/"+username+"/Media/Audio",
    '.wpl' : "/Users/"+username+"/Desktop/"+username+"/Media/Audio",
    '.m3u' : "/Users/"+username+"/Desktop/"+username+"/Media/Audio",
#Text
    '.txt' : "/Users/"+username+"/Desktop/"+username+"/Text/TextFiles",
    '.doc' : "/Users/"+username+"/Desktop/"+username+"/Text/Microsoft/Word",
    '.docx' : "/Users/"+username+"/Desktop/"+username+"/Text/Microsoft/Word",
    '.odt ' : "/Users/"+username+"/Desktop/"+username+"/Text/TextFiles",
    '.pdf': "/Users/"+username+"/Desktop/"+username+"/Text/PDF",
    '.rtf': "/Users/"+username+"/Desktop/"+username+"/Text/TextFiles",
    '.tex': "/Users/"+username+"/Desktop/"+username+"/Text/TextFiles",
    '.wks ': "/Users/"+username+"/Desktop/"+username+"/Text/TextFiles",
    '.wps': "/Users/"+username+"/Desktop/"+username+"/Text/TextFiles",
    '.wpd': "/Users/"+username+"/Desktop/"+username+"/Text/TextFiles",
#Video
    '.3g2': "/Users/"+username+"/Desktop/"+username+"/Media/Video",
    '.3gp': "/Users/"+username+"/Desktop/"+username+"/Media/Video",
    '.avi': "/Users/"+username+"/Desktop/"+username+"/Media/Video",
    '.flv': "/Users/"+username+"/Desktop/"+username+"/Media/Video",
    '.h264': "/Users/"+username+"/Desktop/"+username+"/Media/Video",
    '.m4v': "/Users/"+username+"/Desktop/"+username+"/Media/Video",
    '.mkv': "/Users/"+username+"/Desktop/"+username+"/Media/Video",
    '.mov': "/Users/"+username+"/Desktop/"+username+"/Media/Video",
    '.mp4': "/Users/"+username+"/Desktop/"+username+"/Media/Video",
    '.mpg': "/Users/"+username+"/Desktop/"+username+"/Media/Video",
    '.mpeg': "/Users/"+username+"/Desktop/"+username+"/Media/Video",
    '.rm': "/Users/"+username+"/Desktop/"+username+"/Media/Video",
    '.swf': "/Users/"+username+"/Desktop/"+username+"/Media/Video",
    '.vob': "/Users/"+username+"/Desktop/"+username+"/Media/Video",
    '.wmv': "/Users/"+username+"/Desktop/"+username+"/Media/Video",
#Images
    '.ai': "/Users/"+username+"/Desktop/"+username+"/Media/Images",
    '.bmp': "/Users/"+username+"/Desktop/"+username+"/Media/Images",
    '.gif': "/Users/"+username+"/Desktop/"+username+"/Media/Images",
    '.ico': "/Users/"+username+"/Desktop/"+username+"/Media/Images",
    '.jpg': "/Users/"+username+"/Desktop/"+username+"/Media/Images",
    '.jpeg': "/Users/"+username+"/Desktop/"+username+"/Media/Images",
    '.png': "/Users/"+username+"/Desktop/"+username+"/Media/Images",
    '.ps': "/Users/"+username+"/Desktop/"+username+"/Media/Images",
    '.psd': "/Users/"+username+"/Desktop/"+username+"/Media/Images",
    '.svg': "/Users/"+username+"/Desktop/"+username+"/Media/Images",
    '.tif': "/Users/"+username+"/Desktop/"+username+"/Media/Images",
    '.tiff': "/Users/"+username+"/Desktop/"+username+"/Media/Images",
    '.CR2': "/Users/"+username+"/Desktop/"+username+"/Media/Images",
#Internet
    '.asp': "/Users/"+username+"/Desktop/"+username+"/Other/Internet",
    '.aspx': "/Users/"+username+"/Desktop/"+username+"/Other/Internet",
    '.cer': "/Users/"+username+"/Desktop/"+username+"/Other/Internet",
    '.cfm': "/Users/"+username+"/Desktop/"+username+"/Other/Internet",
    '.cgi': "/Users/"+username+"/Desktop/"+username+"/Other/Internet",
    '.pl': "/Users/"+username+"/Desktop/"+username+"/Other/Internet",
    '.css': "/Users/"+username+"/Desktop/"+username+"/Other/Internet",
    '.htm': "/Users/"+username+"/Desktop/"+username+"/Other/Internet",
    '.js': "/Users/"+username+"/Desktop/"+username+"/Other/Internet",
    '.jsp': "/Users/"+username+"/Desktop/"+username+"/Other/Internet",
    '.part': "/Users/"+username+"/Desktop/"+username+"/Other/Internet",
    '.php': "/Users/"+username+"/Desktop/"+username+"/Other/Internet",
    '.rss': "/Users/"+username+"/Desktop/"+username+"/Other/Internet",
    '.xhtml': "/Users/"+username+"/Desktop/"+username+"/Other/Internet",
    '.html': "/Users/"+username+"/Desktop/"+username+"/Other/Internet",
#Compressed
    '.7z': "/Users/"+username+"/Desktop/"+username+"/Other/Compressed",
    '.arj': "/Users/"+username+"/Desktop/"+username+"/Other/Compressed",
    '.deb': "/Users/"+username+"/Desktop/"+username+"/Other/Compressed",
    '.pkg': "/Users/"+username+"/Desktop/"+username+"/Other/Compressed",
    '.rar': "/Users/"+username+"/Desktop/"+username+"/Other/Compressed",
    '.rpm': "/Users/"+username+"/Desktop/"+username+"/Other/Compressed",
    '.tar.gz': "/Users/"+username+"/Desktop/"+username+"/Other/Compressed",
    '.z': "/Users/"+username+"/Desktop/"+username+"/Other/Compressed",
    '.zip': "/Users/"+username+"/Desktop/"+username+"/Other/Compressed",
#Disc
    '.bin': "/Users/"+username+"/Desktop/"+username+"/Other/Disc",
    '.dmg': "/Users/"+username+"/Desktop/"+username+"/Other/Disc",
    '.iso': "/Users/"+username+"/Desktop/"+username+"/Other/Disc",
    '.toast': "/Users/"+username+"/Desktop/"+username+"/Other/Disc",
    '.vcd': "/Users/"+username+"/Desktop/"+username+"/Other/Disc",
#Data
    '.csv': "/Users/"+username+"/Desktop/"+username+"/Programming/Database",
    '.dat': "/Users/"+username+"/Desktop/"+username+"/Programming/Database",
    '.db': "/Users/"+username+"/Desktop/"+username+"/Programming/Database",
    '.dbf': "/Users/"+username+"/Desktop/"+username+"/Programming/Database",
    '.log': "/Users/"+username+"/Desktop/"+username+"/Programming/Database",
    '.mdb': "/Users/"+username+"/Desktop/"+username+"/Programming/Database",
    '.sav': "/Users/"+username+"/Desktop/"+username+"/Programming/Database",
    '.sql': "/Users/"+username+"/Desktop/"+username+"/Programming/Database",
    '.tar': "/Users/"+username+"/Desktop/"+username+"/Programming/Database",
    '.xml': "/Users/"+username+"/Desktop/"+username+"/Programming/Database",
    '.json': "/Users/"+username+"/Desktop/"+username+"/Programming/Database",
#Executables
    '.apk': "/Users/"+username+"/Desktop/"+username+"/Other/Executables",
    '.bat': "/Users/"+username+"/Desktop/"+username+"/Other/Executables",
    '.com': "/Users/"+username+"/Desktop/"+username+"/Other/Executables",
    '.exe': "/Users/"+username+"/Desktop/"+username+"/Other/Executables",
    '.jar': "/Users/"+username+"/Desktop/"+username+"/Other/Executables",
    '.wsf': "/Users/"+username+"/Desktop/"+username+"/Other/Executables",
#Fonts
    '.fnt': "/Users/"+username+"/Desktop/"+username+"/Other/Fonts",
    '.fon': "/Users/"+username+"/Desktop/"+username+"/Other/Fonts",
    '.otf': "/Users/"+username+"/Desktop/"+username+"/Other/Fonts",
    '.ttf': "/Users/"+username+"/Desktop/"+username+"/Other/Fonts",
#Presentations
    '.key': "/Users/"+username+"/Desktop/"+username+"/Text/Presentations",
    '.odp': "/Users/"+username+"/Desktop/"+username+"/Text/Presentations",
    '.pps': "/Users/"+username+"/Desktop/"+username+"/Text/Presentations",
    '.ppt': "/Users/"+username+"/Desktop/"+username+"/Text/Presentations",
    '.pptx': "/Users/"+username+"/Desktop/"+username+"/Text/Presentations",
#Programming
    '.c': "/Users/"+username+"/Desktop/"+username+"/Programming/C&C++",
    '.class': "/Users/"+username+"/Desktop/"+username+"/Programming/Java",
    '.dart': "/Users/"+username+"/Desktop/"+username+"/Programming/Dart",
    '.py': "/Users/"+username+"/Desktop/"+username+"/Programming/Python",
    '.sh': "/Users/"+username+"/Desktop/"+username+"/Programming/Shell",
    '.swift': "/Users/"+username+"/Desktop/"+username+"/Programming/Swift",
    '.h': "/Users/"+username+"/Desktop/"+username+"/Programming/C&C++",
#Spreadsheets
    '.ods' : "/Users/"+username+"/Desktop/"+username+"/Text/Microsoft/Excel",
    '.xlr' : "/Users/"+username+"/Desktop/"+username+"/Text/Microsoft/Excel",
    '.xls' : "/Users/"+username+"/Desktop/"+username+"/Text/Microsoft/Excel",
    '.xlsx' : "/Users/"+username+"/Desktop/"+username+"/Text/Microsoft/Excel",
#System
    '.bak' : "/Users/"+username+"/Desktop/"+username+"/Text/Other/System",
    '.cab' : "/Users/"+username+"/Desktop/"+username+"/Text/Other/System",
    '.cfg' : "/Users/"+username+"/Desktop/"+username+"/Text/Other/System",
    '.cpl' : "/Users/"+username+"/Desktop/"+username+"/Text/Other/System",
    '.cur' : "/Users/"+username+"/Desktop/"+username+"/Text/Other/System",
    '.dll' : "/Users/"+username+"/Desktop/"+username+"/Text/Other/System",
    '.dmp' : "/Users/"+username+"/Desktop/"+username+"/Text/Other/System",
    '.drv' : "/Users/"+username+"/Desktop/"+username+"/Text/Other/System",
    '.icns' : "/Users/"+username+"/Desktop/"+username+"/Text/Other/System",
    '.ico' : "/Users/"+username+"/Desktop/"+username+"/Text/Other/System",
    '.ini' : "/Users/"+username+"/Desktop/"+username+"/Text/Other/System",
    '.lnk' : "/Users/"+username+"/Desktop/"+username+"/Text/Other/System",
    '.msi' : "/Users/"+username+"/Desktop/"+username+"/Text/Other/System",
    '.sys' : "/Users/"+username+"/Desktop/"+username+"/Text/Other/System",
    '.tmp' : "/Users/"+username+"/Desktop/"+username+"/Text/Other/System",
}


folder_to_track = "/Users/"+username+"/Downloads"
folder_destination = "/Users/"+username+"/Desktop/"+username
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