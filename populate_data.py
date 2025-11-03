import sqlite3
import random
from datetime import datetime, timedelta

# Connect to your database
conn = sqlite3.connect("sql/urban_air_quality.db")
cursor = conn.cursor()

# Define cities and their baseline pollution levels
cities = {
    "Delhi": {"pm25": (120, 250), "pm10": (200, 400), "no2": (40, 80), "so2": (20, 40), "co": (0.8, 1.8), "o3": (30, 60)},
    "Mumbai": {"pm25": (80, 180), "pm10": (150, 300), "no2": (35, 70), "so2": (15, 35), "co": (0.6, 1.2), "o3": (35, 65)},
    "Bangalore": {"pm25": (50, 120), "pm10": (100, 200), "no2": (25, 60), "so2": (10, 25), "co": (0.4, 1.0), "o3": (40, 70)},
}

# Define date range (5 years)
start_date = datetime(2020, 1, 1)
end_date = datetime(2025, 11, 1)
delta = timedelta(days=1)

# Fetch station IDs mapped to cities
cursor.execute("SELECT station_id, city_id FROM station")
stations = cursor.fetchall()
station_map = {cid: sid for sid, cid in stations}

# Function to generate one record
def generate_record(city_name, station_id, date):
    base = cities[city_name]
    pm25 = round(random.uniform(*base["pm25"]), 1)
    pm10 = round(random.uniform(*base["pm10"]), 1)
    no2 = round(random.uniform(*base["no2"]), 1)
    so2 = round(random.uniform(*base["so2"]), 1)
    co = round(random.uniform(*base["co"]), 2)
    o3 = round(random.uniform(*base["o3"]), 1)
    return (station_id, date.strftime("%Y-%m-%d %H:%M:%S"), pm25, pm10, no2, so2, co, o3)

# Generate and insert data
print("Populating data... This may take a moment.")

records = []
date = start_date
while date <= end_date:
    for city, base in cities.items():
        station_id = station_map.get(list(cities.keys()).index(city) + 1)
        records.append(generate_record(city, station_id, date))
    date += delta

cursor.executemany("""
    INSERT INTO air_quality (station_id, datetime, pm25, pm10, no2, so2, co, o3)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", records)

conn.commit()
conn.close()

print(f"✅ Successfully inserted {len(records)} records across {len(cities)} cities.")
