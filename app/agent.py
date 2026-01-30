import time
from monitor import get_system_metrics
from ml_ai import predict_risk

def run_agent():
    while True:
        metrics = get_system_metrics()
        risk = predict_risk(metrics["cpu"], metrics["memory"], metrics["disk"])
        print(f"Metrics: {metrics}, Risk: {risk}")
        time.sleep(10)

if __name__ == "__main__":
    run_agent()
