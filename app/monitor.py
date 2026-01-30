import psutil
import time
import os

start_time = time.time()

def get_system_metrics():
    uptime = time.time() - start_time

    disk_path = "/" if os.name != "nt" else "C:\\"

    metrics = {
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage(disk_path).percent,
        "uptime_seconds": int(uptime)
    }
    return metrics
