import React, { useEffect, useState } from "react";

const API_URL = "http://localhost:8000/sensor-data/";

function App() {
  const [sensorData, setSensorData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(API_URL);
        const data = await response.json();
        setSensorData(data.sensor_data);
      } catch (error) {
        console.error("Error fetching sensor data:", error);
      }
    };

    fetchData();
    const interval = setInterval(fetchData, 5000); // Auto-refresh every 5 seconds

    return () => clearInterval(interval); // Cleanup on unmount
  }, []);

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h2>Live Sensor Data</h2>
      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>Device ID</th>
            <th>Power Usage (kWh)</th>
            <th>Temperature (°C)</th>
            <th>CO₂ (ppm)</th>
          </tr>
        </thead>
        <tbody>
          {sensorData.length > 0 ? (
            sensorData.map((sensor, index) => (
              <tr key={index}>
                <td>{sensor.device_id}</td>
                <td>{sensor.power_usage}</td>
                <td>{sensor.temperature}</td>
                <td>{sensor.co2}</td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="4">No data available</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}

export default App;

