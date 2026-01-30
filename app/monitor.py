import psutil
import time

start_time = time.time()

def get_system_metrics():
    uptime = time.time() - start_time
    metrics = {
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("C:\\").percent,  # Windows path
        "uptime_seconds": int(uptime)
    }
    return metrics
