import sqlite3
import pandas as pd

def load_data_from_sqlite(db_path: str) -> pd.DataFrame:
    """Load joined air quality, station, and city data."""
    conn = sqlite3.connect(db_path)
    query = """
    SELECT aq.*, s.station_name, s.latitude, s.longitude,
           c.city_name, c.country
    FROM air_quality aq
    JOIN station s ON aq.station_id = s.station_id
    JOIN city c ON s.city_id = c.city_id
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df
