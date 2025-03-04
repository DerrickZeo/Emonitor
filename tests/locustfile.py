from locust import HttpUser, task

class LoadTest(HttpUser):
    @task
    def send_sensor_data(self):
        self.client.post("/sensor-data/", json={"device_id": "sensor_001", "power_usage": 3.2, "temperature": 25.5, "co2": 400})