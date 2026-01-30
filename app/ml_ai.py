import os
import joblib
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

MODEL_FILE = "system_monitor_model.pkl"

# Create dummy model if not exists
if not os.path.exists(MODEL_FILE):
    df = pd.DataFrame({
        "cpu": [10, 20, 50, 80],
        "memory": [30, 50, 70, 85],
        "disk": [10, 20, 40, 60],
        "risk": ["Low", "Low", "Medium", "High"]
    })
    X = df[["cpu","memory","disk"]]
    y = df["risk"]
    model = RandomForestClassifier()
    model.fit(X, y)
    joblib.dump(model, MODEL_FILE)

model = joblib.load(MODEL_FILE)

def predict_risk(cpu, memory, disk):
    df_input = pd.DataFrame([[cpu, memory, disk]], columns=["cpu","memory","disk"])
    risk = model.predict(df_input)[0]
    action_map = {
        "Low": "System healthy",
        "Medium": "Scale resources",
        "High": "Restart service"
    }
    return {"risk": risk, "recommended_action": action_map[risk]}
