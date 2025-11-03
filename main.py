from src.db_utils import load_data_from_sqlite
from src.aqi_utils import calculate_aqi
from src.visualizations import create_visualizations
import os

print("🔗 Loading urban air quality data...")
df = load_data_from_sqlite("sql/urban_air_quality.db")
print(f"✅ Loaded {len(df)} records.\n")

print("🧮 Calculating AQI values and categories...")
df = calculate_aqi(df)

print("\n--- AQI Summary ---")
print(df["AQI_Category"].value_counts())

print("\n📈 Generating visualizations...")
create_visualizations(df)

# Save output
os.makedirs("data", exist_ok=True)
output_path = "data/urban_air_quality_aqi.csv"
df.to_csv(output_path, index=False)
print(f"\n✅ Final dataset exported to: {output_path}")
