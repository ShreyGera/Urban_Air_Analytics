import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

def create_visualizations(df):
    os.makedirs("plots", exist_ok=True)
    df["year"] = pd.to_datetime(df["datetime"]).dt.year

    # Yearly trend
    plt.figure(figsize=(10,6))
    sns.lineplot(data=df.groupby(["year","city_name"])["Overall_AQI"].mean().reset_index(),
                 x="year", y="Overall_AQI", hue="city_name", marker="o")
    plt.title("Yearly Average AQI per City")
    plt.savefig("plots/yearly_aqi_trend.png", dpi=300)
    plt.close()

    # AQI Category
    plt.figure(figsize=(8,5))
    sns.countplot(x="AQI_Category", data=df,
                  order=["Good","Satisfactory","Moderate","Poor","Very Poor","Severe"],
                  palette="Spectral")
    plt.title("Overall AQI Category Distribution")
    plt.savefig("plots/aqi_category_distribution.png", dpi=300)
    plt.close()

    # Pollutant correlation
    plt.figure(figsize=(8,6))
    sns.heatmap(df[["pm25","pm10","no2","so2","co","o3"]].corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation between Pollutants")
    plt.savefig("plots/pollutant_correlation_heatmap.png", dpi=300)
    plt.close()

    print("📊 Visualizations saved to 'plots/' folder.")
