from dotenv import load_dotenv
from watchdog.observers import Observer
from watchdog.events import  LoggingEventHandler

import os
import json
import time
import logging


if __name__ == "__main__":
    load_dotenv()
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
                        
    folder_to_track = os.environ.get("ENV_FOLDER_TO_TRACK")

    event_handler = LoggingEventHandler()

    observer = Observer()
    observer.schedule(event_handler, folder_to_track, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()