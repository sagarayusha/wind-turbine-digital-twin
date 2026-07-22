from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import math
import numpy as np

app = FastAPI(title="Wind Turbine Digital Twin & Analytics API", version="0.1.0")

# CORS Middleware Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TelemetryData(BaseModel):
    wind_speed: float         # in m/s
    power_output: float       # in Watts
    blade_radius: float = 50.0 # in meters
    air_density: float = 1.225 # in kg/m^3
    vibration_rms: float = 0.5
    temperature_c: float = 45.2
    stress_mpa: float = 120.0

@app.get("/")
def home():
    return {"message": "Wind Turbine Digital Twin Backend is Live!"}

@app.post("/api/v1/predict-analytics")
def predict_analytics(data: TelemetryData):
    if data.wind_speed <= 0:
        raise HTTPException(status_code=400, detail="Wind speed must be greater than zero.")
    
    # Calculations
    swept_area = math.pi * (data.blade_radius ** 2)
    wind_power = 0.5 * data.air_density * swept_area * (data.wind_speed ** 3)
    
    efficiency = (data.power_output / wind_power) * 100 if wind_power > 0 else 0
    efficiency = min(max(efficiency, 0.0), 100.0)
    
    # Estimated Remaining Useful Life (RUL)
    rul = max(1000 - ((data.stress_mpa * 1.5) + (data.temperature_c * 2) + (data.vibration_rms * 100)), 50)
    
    # Emergency Alert & Trip Logic
    is_emergency = False
    warning_message = "Optimal"
    
    if data.temperature_c > 80.0:
        is_emergency = True
        warning_message = "CRITICAL ALERT: Overheating detected! Emergency shutdown initiated."
    elif data.vibration_rms > 1.5:
        is_emergency = True
        warning_message = "CRITICAL ALERT: High mechanical vibration! Braking system engaged."
    elif rul < 150:
        is_emergency = True
        warning_message = "WARNING: Remaining Useful Life (RUL) critically low. Schedule maintenance."
    elif efficiency <= 20 or data.vibration_rms >= 1.0:
        warning_message = "Warning / High Wear"

    return {
        "efficiency_percent": round(efficiency, 2),
        "wind_power_watts": round(wind_power, 2),
        "estimated_remaining_useful_life_hours": round(rul, 2),
        "turbine_status": warning_message,
        "emergency_trip": is_emergency
    }