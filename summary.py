import pandas as pd
import os

# Ensuring processed folder exists
os.makedirs("data/processed", exist_ok=True)

# Load master analytics table
df = pd.read_csv("data/processed/master_transportation_analytics.csv")

# Cost per km by route type
route_cost = df.groupby("route_type")["cost_per_km"].mean().reset_index()
route_cost.columns = ["Route Type", "Average Cost per Km"]

# High cost vs low cost trips
avg_cost = df["cost_per_km"].mean()
df["Cost Category"] = df["cost_per_km"].apply(
    lambda x: "High Cost" if x > avg_cost else "Low Cost"
)
cost_category_summary = df["Cost Category"].value_counts().reset_index()
cost_category_summary.columns = ["Cost Category", "Trip Count"]

# Ranking Vehicle fuel efficiency
vehicle_eff = df.groupby("vehicle_id")["fuel_efficiency_kmpl"].mean().reset_index()
vehicle_eff = vehicle_eff.sort_values(by="fuel_efficiency_kmpl", ascending=False)
vehicle_eff.columns = ["Vehicle ID", "Average Fuel Efficiency (Km/L)"]

# 4. Driver efficiency classification
avg_eff = df["fuel_efficiency_kmpl"].mean()
df["Driver Efficiency"] = df["fuel_efficiency_kmpl"].apply(
    lambda x: "Efficient" if x >= avg_eff else "Inefficient"
)
driver_eff_summary = df.groupby("Driver Efficiency").size().reset_index(name="Count")

# 5. Save all tables to Excel with separate sheets
with pd.ExcelWriter("data/processed/summary_tables.xlsx") as writer:
    route_cost.to_excel(writer, sheet_name="Route Cost", index=False)
    cost_category_summary.to_excel(writer, sheet_name="Trip Cost Category", index=False)
    vehicle_eff.to_excel(writer, sheet_name="Vehicle Efficiency", index=False)
    driver_eff_summary.to_excel(writer, sheet_name="Driver Efficiency", index=False)

#Save a CSV of vehicle ranking
vehicle_eff.to_csv("data/processed/vehicle_efficiency_ranking.csv", index=False)

print("Summary tables saved successfully in Excel and CSV")
