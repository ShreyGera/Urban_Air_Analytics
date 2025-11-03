import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Load and prepare data
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/urban_air_quality_aqi.csv")
    df["datetime"] = pd.to_datetime(df["datetime"])
    df["year"] = df["datetime"].dt.year
    df["month"] = df["datetime"].dt.month
    return df

df = load_data()

# -----------------------------
# Dashboard layout
# -----------------------------
st.set_page_config(page_title="Urban Air Analytics Dashboard", layout="wide")
st.title("Urban Air Analytics Dashboard")
st.markdown("#### Interactive AQI Insights Based on CPCB (India) Standards")

# Sidebar filters
st.sidebar.header("Filters")
selected_city = st.sidebar.selectbox("Select City:", sorted(df["city_name"].unique()))
selected_year = st.sidebar.selectbox("Select Year:", sorted(df["year"].unique()))

filtered_df = df[(df["city_name"] == selected_city) & (df["year"] == selected_year)]

# -----------------------------
# KPI Metrics
# -----------------------------
avg_aqi = filtered_df["Overall_AQI"].mean()
max_aqi = filtered_df["Overall_AQI"].max()
dominant_category = filtered_df["AQI_Category"].mode()[0]

st.subheader(f"📊 Summary for {selected_city} ({selected_year})")
col1, col2, col3 = st.columns(3)
col1.metric("Average AQI", f"{avg_aqi:.1f}")
col2.metric("Max AQI", f"{max_aqi:.1f}")
col3.metric("Dominant Category", dominant_category)

# -----------------------------
# AQI Trend Over Time
# -----------------------------
st.markdown("### AQI Trend Over Time")
fig_trend = px.line(filtered_df, x="datetime", y="Overall_AQI", 
                    title=f"AQI Trend for {selected_city} in {selected_year}",
                    markers=True, color_discrete_sequence=["#FF5733"])
st.plotly_chart(fig_trend, use_container_width=True)

# -----------------------------
# AQI Category Distribution
# -----------------------------
st.markdown("### AQI Category Distribution")
fig_cat = px.histogram(filtered_df, x="AQI_Category", color="AQI_Category",
                       category_orders={"AQI_Category": ["Good","Satisfactory","Moderate","Poor","Very Poor","Severe"]},
                       title=f"AQI Category Distribution - {selected_city} ({selected_year})")
st.plotly_chart(fig_cat, use_container_width=True)

# -----------------------------
# Pollutant-wise Comparison
# -----------------------------
st.markdown("### Pollutant Concentrations")
pollutants = ["pm25", "pm10", "no2", "so2", "co", "o3"]
fig_poll = px.box(filtered_df, y=pollutants, title="Pollutant Concentration Levels", points="all")
st.plotly_chart(fig_poll, use_container_width=True)

# -----------------------------
# Monthly AQI averages
# -----------------------------
st.markdown("### Monthly AQI Averages")
monthly_avg = filtered_df.groupby("month")["Overall_AQI"].mean().reset_index()
fig_month = px.bar(monthly_avg, x="month", y="Overall_AQI", 
                   title="Monthly Average AQI", text_auto=True)
st.plotly_chart(fig_month, use_container_width=True)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Developed by Shrey Gera • Urban Air Analytics © 2025 • Powered by Streamlit & Plotly")
