import time
import threading
from .monitor import get_system_metrics
from .ml_ai import predict_risk

def check_alert(risk):
    if risk["risk"] == "Medium":
        print("⚠️ Warning: Scale resources")
    elif risk["risk"] == "High":
        print("🔥 Critical: Restart service")
    else:
        print("✅ System healthy")

def run_continuous_monitor(interval=10):
    while True:
        try:
            metrics = get_system_metrics()
            risk = predict_risk(
                metrics["cpu"],
                metrics["memory"],
                metrics["disk"]
            )
            check_alert(risk)
        except Exception as e:
            print("Background agent error:", e)

        time.sleep(interval)

# ✅ function to start agent in a separate thread
def start_agent():
    thread = threading.Thread(
        target=run_continuous_monitor,
        daemon=True
    )
    thread.start()
