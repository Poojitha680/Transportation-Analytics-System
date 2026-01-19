import streamlit as st
import pandas as pd
from PIL import Image
import os

# Page Configuration
st.set_page_config(
    page_title="Transportation Analytics Dashboard",
    page_icon="",
    layout="wide"
)

st.title("Transportation Analytics Dashboard")
st.markdown("""
This dashboard provides insights into:
- Fuel efficiency
- Route costs
- Delivery delays
- Vehicle & driver performance
""")

# Load Data
master_file = "data/processed/master_transportation_analytics.csv"
vehicle_csv = "data/processed/vehicle_efficiency_ranking.csv"

df = pd.read_csv(master_file)
vehicle_eff = pd.read_csv(vehicle_csv)

#Sidebar Filters
st.sidebar.header("Filters")

route_options = df['route_type'].unique()
selected_route = st.sidebar.multiselect("Select Route Type", route_options, default=route_options)

driver_options = df['driver_name'].unique()
selected_driver = st.sidebar.multiselect("Select Driver", driver_options, default=driver_options)

df_filtered = df[(df['route_type'].isin(selected_route)) & (df['driver_name'].isin(selected_driver))]

#Key Metrics
st.header("Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Average Fuel Efficiency (Km/L)", round(df_filtered["fuel_efficiency_kmpl"].mean(),2))
col2.metric("Average Cost per Km", round(df_filtered["cost_per_km"].mean(),2))
col3.metric("Average Delivery Delay (min)", round(df_filtered["delivery_delay_minutes"].mean(),2))
col4.metric("Average Maintenance Cost", round(df_filtered["maintenance_cost"].mean(),2))

#Visualizations
st.header("Visualizations")

# Fuel Efficiency by Vehicle
st.subheader("Fuel Efficiency by Vehicle")
fuel_img_path = "visuals/fuel_efficiency_by_vehicle.png"
if os.path.exists(fuel_img_path):
    st.image(fuel_img_path, use_column_width=True)

# Delivery Delay Distribution
st.subheader("Delivery Delay Distribution")
delay_img_path = "visuals/delivery_delay_distribution.png"
if os.path.exists(delay_img_path):
    st.image(delay_img_path, use_column_width=True)

# Cost per Km by Route Type
st.subheader("Cost per Km by Route Type")
cost_img_path = "visuals/cost_per_km_by_route.png"
if os.path.exists(cost_img_path):
    st.image(cost_img_path, use_column_width=True)

# Driver Performance Ranking
st.subheader("Driver Performance Ranking")
driver_img_path = "visuals/driver_performance.png"
if os.path.exists(driver_img_path):
    st.image(driver_img_path, use_column_width=True)

# Correlation Heatmap
st.subheader("Correlation Heatmap")
corr_img_path = "visuals/correlation_heatmap.png"
if os.path.exists(corr_img_path):
    st.image(corr_img_path, use_column_width=True)

# 6. Show Data Table
st.header("Master Table Data")
st.dataframe(df_filtered)

# For Download Summary Tables
st.header("Download Summary Tables")

summary_excel = "data/processed/summary_tables.xlsx"
if os.path.exists(summary_excel):
    with open(summary_excel, "rb") as f:
        st.download_button(
            label="Download Excel Summary Tables",
            data=f,
            file_name="summary_tables.xlsx"
        )

vehicle_csv = "data/processed/vehicle_efficiency_ranking.csv"
if os.path.exists(vehicle_csv):
    with open(vehicle_csv, "rb") as f:
        st.download_button(
            label="Download Vehicle Efficiency CSV",
            data=f,
            file_name="vehicle_efficiency_ranking.csv"
        )

st.markdown("---")
st.markdown("© 2026 Transportation Analytics Dashboard")
