from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

class SensorData(BaseModel):
    device_id: str
    power_usage: float
    temperature: float
    co2: float

def get_db_connection():
    return psycopg2.connect(
        dbname="energy_monitoring",
        user="user",
        password="password",
        host="db",
        port="5432"
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/sensor-data/")
async def get_sensor_data():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT device_id, power_usage, temperature, co2 FROM sensor_data ORDER BY id DESC LIMIT 10")
    rows = cursor.fetchall()

    data = [
        {"device_id": row[0], "power_usage": row[1], "temperature": row[2], "co2": row[3]}
        for row in rows
    ]

    cursor.close()
    conn.close()
    return {"sensor_data": data}

@app.get("/sensor-data/")
async def get_sensor_data():
    """Retrieves the latest 10 sensor readings"""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT device_id, power_usage, temperature, co2 FROM sensor_data ORDER BY id DESC LIMIT 10")
    rows = cursor.fetchall()

    data = [
        {"device_id": row[0], "power_usage": row[1], "temperature": row[2], "co2": row[3]}
        for row in rows
    ]

    cursor.close()
    conn.close()
    return {"sensor_data": data}
