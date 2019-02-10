import datetime
import sys
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from Utils import IOUtils, LoggingUtils


class EventHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        # Create the correct format for the monitor log.
        entryLog = "{}|{}|{}\n".format(
            datetime.datetime.now().isoformat(),
            event.event_type,
            event.src_path)

        print(entryLog)
        IOUtils.write("C:\\Users\\HpServer\\Desktop\\LazyReplicationTool\\DirectoryMonitor.log", entryLog)


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'

    LoggingUtils.log('Directory Monitor is starting for the path: ' + path)

    event_handler = EventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
