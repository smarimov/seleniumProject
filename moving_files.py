from watchdog.observers import *
from watchdog.events import FileSystemEventHandler
import os
import json
import time


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = f'{folder_to_track} /+{filename}'
            new_destination = f'{folder_destination}/ {filename}'
            os.rename(src, new_destination)


folder_to_track = "C:\\Users\\shoki\\OneDrive\\Desktop\\Class"
folder_destination = "C:\\Users\\shoki\\OneDrive\\Desktop\\New folder"

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler,folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()