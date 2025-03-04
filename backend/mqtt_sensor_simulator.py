import paho.mqtt.client as mqtt
import random
import time
import json
import os

# Automatically determine the correct broker
BROKER = os.getenv("MQTT_BROKER", "mosquitto_broker")  # Default to Docker hostname
PORT = 1883
TOPIC = "emonitoring/sensors"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to MQTT Broker!")
    else:
        print(f"⚠️ Failed to connect, return code {rc}")

client = mqtt.Client()
client.on_connect = on_connect

while True:
    try:
        print(f"🔄 Connecting to MQTT broker at {BROKER}...")
        client.connect(BROKER, PORT, 60)  # Try to connect
        break
    except Exception as e:
        print(f"⚠️ Connection failed: {e}. Retrying in 5 seconds...")
        time.sleep(5)

print("🔹 MQTT Sensor Simulator Started...")

while True:
    data = {
        "device_id": "sensor_001",
        "power_usage": round(random.uniform(1.0, 5.0), 2),
        "temperature": round(random.uniform(20.0, 35.0), 2),
        "co2": round(random.uniform(300, 600), 2),
    }
    client.publish(TOPIC, json.dumps(data))
    print(f"📡 Published: {data}")
    time.sleep(5)
