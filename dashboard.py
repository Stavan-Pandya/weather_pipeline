import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

st.set_page_config(page_title="Weather Dashboard", layout="wide")

st.markdown("""
<style>
h1 {font-size: 28px;}
h2, h3 {font-size: 20px;}
[data-testid="stMetricLabel"] {font-size: 13px;}
[data-testid="stMetricValue"] {font-size: 22px;}
.block-container {padding-top: 1.5rem;}
</style>
""", unsafe_allow_html=True)

st.title("Weather Analytics Dashboard")

engine = create_engine("sqlite:///database/weather.db")
df = pd.read_sql("SELECT * FROM weather", engine)
df["timestamp"] = pd.to_datetime(df["timestamp"])

st.sidebar.title("Filters")

selected_cities = st.sidebar.multiselect(
    "Cities",
    options=sorted(df["city"].unique()),
    default=sorted(df["city"].unique())
)

filtered_df = df[df["city"].isin(selected_cities)]

st.sidebar.download_button(
    "Download CSV",
    filtered_df.to_csv(index=False),
    "weather_data.csv",
    "text/csv"
)

latest_df = (
    filtered_df.sort_values("timestamp")
    .groupby("city")
    .tail(1)
)

k1, k2, k3, k4, k5 = st.columns(5)

k1.metric("Records", len(filtered_df))
k2.metric("Cities", filtered_df["city"].nunique())
k3.metric("Avg Temp", f"{filtered_df['temperature'].mean():.1f} °C")
k4.metric("Max Temp", f"{filtered_df['temperature'].max():.1f} °C")
k5.metric("Avg Humidity", f"{filtered_df['humidity'].mean():.1f}%")

st.divider()

st.subheader("Latest City Weather")

card_cols = st.columns(len(latest_df))

for col, (_, row) in zip(card_cols, latest_df.iterrows()):
    with col:
        st.metric(row["city"], f"{row['temperature']} °C")
        st.caption(f"{row['weather']} | Humidity {row['humidity']}%")

st.divider()

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("Average Temperature")

    avg_temp = (
        filtered_df.groupby("city")["temperature"]
        .mean()
        .reset_index()
    )

    fig1, ax1 = plt.subplots(figsize=(4.8, 2.8))
    ax1.bar(avg_temp["city"], avg_temp["temperature"])
    ax1.set_ylabel("°C", fontsize=8)
    ax1.tick_params(axis="x", labelrotation=30, labelsize=8)
    ax1.tick_params(axis="y", labelsize=8)
    ax1.set_title("")
    plt.tight_layout()
    st.pyplot(fig1, use_container_width=True)

with chart_col2:
    st.subheader("Average Humidity")

    avg_humidity = (
        filtered_df.groupby("city")["humidity"]
        .mean()
        .reset_index()
    )

    fig2, ax2 = plt.subplots(figsize=(4.8, 2.8))
    ax2.bar(avg_humidity["city"], avg_humidity["humidity"])
    ax2.set_ylabel("%", fontsize=8)
    ax2.tick_params(axis="x", labelrotation=30, labelsize=8)
    ax2.tick_params(axis="y", labelsize=8)
    ax2.set_title("")
    plt.tight_layout()
    st.pyplot(fig2, use_container_width=True)

trend_col, scatter_col = st.columns(2)

with trend_col:
    st.subheader("Temperature Trend")

    selected_city = st.selectbox(
        "Select city",
        sorted(filtered_df["city"].unique())
    )

    city_df = filtered_df[
        filtered_df["city"] == selected_city
    ].sort_values("timestamp")

    fig3, ax3 = plt.subplots(figsize=(4.8, 2.8))
    ax3.plot(city_df["timestamp"], city_df["temperature"], marker="o")
    ax3.set_ylabel("°C", fontsize=8)
    ax3.tick_params(axis="x", labelrotation=30, labelsize=7)
    ax3.tick_params(axis="y", labelsize=8)
    ax3.set_title("")
    plt.tight_layout()
    st.pyplot(fig3, use_container_width=True)

with scatter_col:
    st.subheader("Humidity vs Temperature")

    fig4, ax4 = plt.subplots(figsize=(4.8, 2.8))
    ax4.scatter(filtered_df["temperature"], filtered_df["humidity"])
    ax4.set_xlabel("Temperature °C", fontsize=8)
    ax4.set_ylabel("Humidity %", fontsize=8)
    ax4.tick_params(axis="both", labelsize=8)
    ax4.set_title("")
    plt.tight_layout()
    st.pyplot(fig4, use_container_width=True)

st.divider()

hot_city = latest_df.loc[latest_df["temperature"].idxmax()]
cool_city = latest_df.loc[latest_df["temperature"].idxmin()]

i1, i2 = st.columns(2)

i1.success(f"Hottest city: {hot_city['city']} — {hot_city['temperature']} °C")
i2.info(f"Coolest city: {cool_city['city']} — {cool_city['temperature']} °C")

with st.expander("View Raw Data"):
    st.dataframe(filtered_df, use_container_width=True)

with st.expander("Run SQL Query"):
    default_query = """
SELECT city, AVG(temperature) AS avg_temp
FROM weather
GROUP BY city;
"""
    sql_query = st.text_area("SQL", default_query, height=120)

    if st.button("Run Query"):
        try:
            result = pd.read_sql(sql_query, engine)
            st.dataframe(result, use_container_width=True)
        except Exception as e:
            
            st.error(e)