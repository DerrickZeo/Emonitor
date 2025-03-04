import paho.mqtt.client as mqtt
import psycopg2
import json
import os
import time

BROKER = os.getenv("MQTT_BROKER", "mosquitto_broker")  # Use correct service name
TOPIC = "emonitoring/sensors"

def get_db_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME", "energy_monitoring"),
        user=os.getenv("DB_USER", "user"),
        password=os.getenv("DB_PASSWORD", "password"),
        host=os.getenv("DB_HOST", "db"),
        port="5432"
    )

def on_message(client, userdata, message):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        data = json.loads(message.payload.decode())

        cursor.execute(
            "INSERT INTO sensor_data (device_id, power_usage, temperature, co2) VALUES (%s, %s, %s, %s)",
            (data["device_id"], data["power_usage"], data["temperature"], data["co2"])
        )

        conn.commit()
        cursor.close()
        conn.close()
        print(f"✅ Data Saved: {data}")
    except Exception as e:
        print(f"⚠️ Error saving data: {e}")

client = mqtt.Client()
client.connect(BROKER, 1883, 60)
client.subscribe(TOPIC)

client.on_message = on_message
print("🔹 Listening for MQTT messages and saving to DB...")
client.loop_forever()
