import pytest
from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_get_sensor_data():
    """Test that FastAPI `/sensor-data/` endpoint returns valid data."""
    response = client.get("/sensor-data/")
    assert response.status_code == 200
    data = response.json()
    assert "sensor_data" in data
    assert isinstance(data["sensor_data"], list)

def test_post_sensor_data():
    """Test that we can insert sensor data into the database."""
    payload = {
        "device_id": "sensor_test",
        "power_usage": 3.5,
        "temperature": 22.0,
        "co2": 400
    }
    response = client.post("/sensor-data/", json=payload)
    assert response.status_code == 200
    assert response.json() == {"status": "success"}

