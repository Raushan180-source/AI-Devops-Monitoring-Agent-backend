import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

logging.basicConfig(filename="app.log", level=logging.INFO)

class LogHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("app.log"):
            with open(event.src_path, "r") as f:
                lines = f.readlines()[-5:]  # last 5 lines
            for line in lines:
                if "ERROR" in line or "WARNING" in line:
                    print("Alert log:", line)

def start_log_monitor():
    observer = Observer()
    observer.schedule(LogHandler(), ".", recursive=False)
    observer.start()
