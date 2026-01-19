import pandas as pd

# Loading master data
df = pd.read_csv("data/processed/master_transportation_analytics.csv")

# Cost per km by route type
route_cost = df.groupby("route_type")["cost_per_km"].mean().reset_index()
route_cost.columns = ["route_type", "avg_cost_per_km"]
print("\nAverage Cost per Km by Route Type")
print(route_cost)

# Comparision of High cost and Low cost trips
avg_cost = df["cost_per_km"].mean()

df["cost_category"] = df["cost_per_km"].apply(
    lambda x: "High Cost" if x > avg_cost else "Low Cost"
)

print("\nCost Category Count")
print(df["cost_category"].value_counts())

# 3. Vehicle fuel efficiency ranking
vehicle_eff = df.groupby("vehicle_id")["fuel_efficiency_kmpl"].mean().reset_index()
vehicle_eff = vehicle_eff.sort_values(by="fuel_efficiency_kmpl", ascending=False)

print("\nVehicle Fuel Efficiency Ranking")
print(vehicle_eff)

# 4. Driver efficiency classification
avg_eff = df["fuel_efficiency_kmpl"].mean()

df["driver_efficiency"] = df["fuel_efficiency_kmpl"].apply(
    lambda x: "Efficient" if x >= avg_eff else "Inefficient"
)

print("\nDriver Efficiency Summary")
print(df.groupby("driver_efficiency").size())
