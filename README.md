# Urban Air Analytics

## Overview

**Urban Air Analytics** is a data-driven project that analyzes urban air quality across major Indian cities.
It computes the **Air Quality Index (AQI)** based on scientifically accurate **CPCB (Central Pollution Control Board)** standards, generates pollutant-level insights, and visualizes temporal and spatial trends using **Python**, **SQLite**, and **Matplotlib**.

The project enables environmental data analysis by integrating raw air quality data, calculating pollutant sub-indices, determining overall AQI, and providing interpretive plots for better decision-making.

---

## Project Structure

```
Urban_Air_Analytics/
│
├── data/                         # Stores cleaned and processed CSV files
│   ├── urban_air_quality_clean.csv
│   └── urban_air_quality_aqi.csv
│
├── plots/                        # Auto-generated visualizations
│   ├── yearly_aqi_trend.png
│   ├── pollutant_correlation_heatmap.png
│   ├── aqi_category_distribution.png
│   └── top10_polluted_days_per_city.png
│
├── sql/                          # SQLite database files
│   └── urban_air_quality.db
│
├── src/                          # Source Python modules
│   ├── __init__.py
│   ├── db_utils.py               # Database loading functions
│   ├── aqi_utils.py              # AQI computation logic
│   └── visualizations.py         # Visualization generation
│
├── main.py                       # Main pipeline script
├── populate_data.py              # Script to populate SQLite database
├── .gitignore
└── README.md
```

---

## Features

* Reads and integrates air quality data from SQLite database.
* Computes AQI values for six key pollutants: **PM2.5, PM10, NO₂, SO₂, CO, and O₃**.
* Applies **CPCB AQI Breakpoints** for accurate sub-index computation.
* Generates detailed plots:

  * Yearly AQI trends per city
  * Correlation between pollutants
  * AQI category distributions
  * Top 10 most polluted days per city
* Exports a clean and processed dataset with computed AQI and category.

---

## AQI Calculation Methodology

AQI Calculation Methodology

The Air Quality Index (AQI) is calculated using pollutant concentration breakpoints defined by the Central Pollution Control Board (CPCB, India).
Each pollutant’s sub-index is calculated using linear interpolation as follows:

```math
I_p = \frac{(I_{HI} - I_{LO})}{(BP_{HI} - BP_{LO})} \times (C_p - BP_{LO}) + I_{LO}
```
Where:

```math
\text{Where:} \\
I_p = \text{AQI sub-index for pollutant } p \\
C_p = \text{Observed pollutant concentration} \\
BP_{HI}, BP_{LO} = \text{Upper and lower breakpoint concentrations for the pollutant} \\
I_{HI}, I_{LO} = \text{AQI index range corresponding to those breakpoints}
```

The overall AQI for a monitoring station is taken as the **maximum** of the sub-indices of all pollutants measured at that location.

---

### CPCB AQI Categories

| AQI Range | Category     | Health Impact                              |
| --------- | ------------ | ------------------------------------------ |
| 0–50      | Good         | Minimal impact                             |
| 51–100    | Satisfactory | Minor breathing discomfort                 |
| 101–200   | Moderate     | Breathing discomfort for sensitive groups  |
| 201–300   | Poor         | Respiratory illness on prolonged exposure  |
| 301–400   | Very Poor    | Increased respiratory issues               |
| 401–500   | Severe       | Health effects even on healthy individuals |

---

## How to Run

### 1. Setup the Environment

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Populate Database

```bash
python populate_data.py
```

### 3. Run Main Script

```bash
python main.py
```

The script will automatically:

* Load data from SQLite
* Compute AQI values
* Generate visualizations in `plots/`
* Export the cleaned dataset to `data/`

---

## Dependencies

* Python 3.10+
* pandas
* numpy
* matplotlib
* seaborn
* sqlite3

---

## Outputs

* **urban_air_quality_aqi.csv** — Final dataset containing pollutant readings, sub-indices, and overall AQI.
* **Plots** — Auto-generated charts visualizing AQI and pollutant relationships.

---

## Future Scope

* Integration with real-time API data sources (CPCB or OpenAQ).
* Deployment of dashboards using Power BI or Streamlit.
* Predictive modeling of AQI using machine learning techniques.

---

## Author

**Shrey Gera**
Engineering Student — AI and Data Science

---