import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("visuals", exist_ok=True)
# Loading master analytics table
df = pd.read_csv("data/processed/master_transportation_analytics.csv")

print(df.head())
print(df.describe())

#Fuel Efficiency by Vehicle
plt.figure(figsize=(8,5))
sns.barplot(
    x="vehicle_id",
    y="fuel_efficiency_kmpl",
    data=df
)
plt.title("Fuel Efficiency by Vehicle")
plt.ylabel("Km per Liter")
plt.xlabel("Vehicle ID")
plt.tight_layout()
plt.savefig("visuals/fuel_efficiency_by_vehicle.png")
plt.close()

# Delivery Delay Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["delivery_delay_minutes"], bins=5, kde=True)
plt.title("Delivery Delay Distribution")
plt.xlabel("Delay (minutes)")
plt.ylabel("Trip Count")
plt.tight_layout()
plt.savefig("visuals/delivery_delay_distribution.png")
plt.close()

# 4. Route Type vs Cost per Km
plt.figure(figsize=(8,5))
sns.boxplot(
    x="route_type",
    y="cost_per_km",
    data=df
)
plt.title("Cost per Km by Route Type")
plt.xlabel("Route Type")
plt.ylabel("Cost per Km")
plt.tight_layout()
plt.savefig("visuals/cost_per_km_by_route.png")
plt.close()

# 5. Driver Performance Ranking
driver_perf = df.groupby("driver_name")["driver_performance_score"].mean().reset_index()

plt.figure(figsize=(8,5))
sns.barplot(
    x="driver_performance_score",
    y="driver_name",
    data=driver_perf
)
plt.title("Average Driver Performance Score")
plt.xlabel("Performance Score")
plt.ylabel("Driver")
plt.tight_layout()
plt.savefig("visuals/driver_performance.png")
plt.close()

# Creating Correlation Heatmap
plt.figure(figsize=(10,6))
numeric_cols = df.select_dtypes(include="number")
sns.heatmap(
    numeric_cols.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("visuals/correlation_heatmap.png")
plt.close()

print("EDA and visualizations completed successfully!")
