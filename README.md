# 🌪️ Wind Turbine Digital Twin & Analytics Dashboard

An industrial IoT and predictive maintenance web application designed for real-time asset monitoring[cite: 1]. It bridges live telemetry inputs—such as wind speed, vibration, temperature, and mechanical stress—with computational analytics to track turbine operational efficiency, predict Remaining Useful Life (RUL), and execute automated emergency safety shutdowns[cite: 1, 2].

---

## 🚀 Key Features
* **Real-Time Telemetry Processing:** FastAPI backend calculates aerodynamic wind power, efficiency percentages, and mechanical wear based on live sensor inputs[cite: 2].
* **Predictive Maintenance & RUL:** Estimates Remaining Useful Life (RUL) dynamically using stress, temperature, and vibration metrics[cite: 2].
* **Automated Emergency Trip System:** Triggers critical safety trips and halts 3D blade rotation instantly when thresholds exceed safe operational limits[cite: 2].
* **Interactive 3D Viewport:** A WebGL-accelerated Three.js digital twin canvas featuring dynamic speed control linked directly to system operational status[cite: 2].

---

## 🛠️ Technical Architecture & Stack
* **Backend Framework:** Python, FastAPI, Pydantic, Uvicorn, NumPy, Scikit-Learn[cite: 2]
* **Frontend Interface:** HTML5, CSS3, Modern JavaScript (ES6+), Three.js (WebGL rendering engine)[cite: 2]
* **Communication Protocol:** RESTful JSON APIs transmitted over HTTP with CORS middleware enabled[cite: 2]

---

## ⚙️ How to Run Locally

### 1. Clone the Repository
```bash
git clone [https://github.com/sagarayusha/wind-turbine-digital-twin.git](https://github.com/sagarayusha/wind-turbine-digital-twin.git)
cd wind-turbine-digital-twin
