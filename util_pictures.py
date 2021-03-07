from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print("Found something!")
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)

# def ObserveFolder():

if __name__ == "__main__":
    # ObserveFolder()
    print("This works")
    folder_to_track = "C:/Users/drg65/Desktop/My Personal Projects/Python Projects/PROJECT Bahamut/Portal"
    folder_destination = "C:/Users/drg65/Desktop/My Personal Projects/Python Projects/PROJECT Bahamut/Destination"

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