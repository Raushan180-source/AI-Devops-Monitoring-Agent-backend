from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .monitor import get_system_metrics
from .ml_ai import predict_risk
from .background_agent import start_agent

app = FastAPI(title="Hackathon System Monitor")

# 🔹 CORS setup (for React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 Start background agent
start_agent()

@app.get("/")
def root():
    return {"message": "System Monitor Backend Running"}

# 🔹 THIS ENDPOINT MATCHES Dashboard.js
@app.get("/metrics")
def metrics():
    metrics = get_system_metrics()

    risk = predict_risk(
        metrics["cpu"],
        metrics["memory"],
        metrics["disk"]
    )

    return {
        "metrics": metrics,
        "risk": risk
    }
