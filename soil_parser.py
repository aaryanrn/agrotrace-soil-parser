import json
import random
from datetime import datetime
import os

# Simulate parsing data
data = {
    "timestamp": str(datetime.now()),
    "sensor_id": "WINDOWS-SENSOR-001",
    "soil_ph": round(random.uniform(5.5, 7.5), 2),
    "moisture_level": "Optimal",
    "status": "PROCESSED"
}

# Write JSON file
filename = "soil_data.json"
with open(filename, "w") as f:
    json.dump(data, f, indent=4)

print(f"Data successfully parsed to {os.path.abspath(filename)}")

# Testing Webhook 
