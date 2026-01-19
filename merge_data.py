import pandas as pd
import os

# Ensure output folder exists
os.makedirs("data/processed", exist_ok=True)

# 1. LOAD DATA
vehicles = pd.read_csv("data/raw/vehicles.csv")
drivers = pd.read_csv("data/raw/drivers.csv")
trips = pd.read_csv("data/raw/trips.csv")
fuel = pd.read_csv("data/raw/fuel_logs.csv")
gps = pd.read_csv("data/raw/gps_routes.csv")
maintenance = pd.read_csv("data/raw/maintenance.csv")

# DATA CLEANING
trips["trip_date"] = pd.to_datetime(trips["trip_date"])
maintenance["maintenance_date"] = pd.to_datetime(maintenance["maintenance_date"])

# Fill missing values if any exists
fuel.fillna(0, inplace=True)
gps.fillna(0, inplace=True)
maintenance["maintenance_cost"].fillna(0, inplace=True)

# MERGE DATASETS
master = trips.merge(vehicles, on="vehicle_id", how="left") \
              .merge(drivers, on="driver_id", how="left") \
              .merge(fuel, on="trip_id", how="left") \
              .merge(gps, on="trip_id", how="left") \
              .merge(maintenance, on="vehicle_id", how="left")

# FEATURE ENGINEERING
master["fuel_efficiency_kmpl"] = master["distance_km"] / master["fuel_consumed_liters"]
master["fuel_cost"] = master["fuel_consumed_liters"] * master["fuel_cost_per_liter"]
master["total_trip_cost"] = master["fuel_cost"] + master["maintenance_cost"]
master["cost_per_km"] = master["total_trip_cost"] / master["distance_km"]

# Driver performance score (simple business logic)
master["driver_performance_score"] = (
    (master["fuel_efficiency_kmpl"] * 2) -
    (master["delivery_delay_minutes"] / 10)
)

# 5. FINAL COLUMN SELECTION
final_columns = [
    "trip_id",
    "trip_date",
    "vehicle_id",
    "driver_id",
    "driver_name",
    "route_type",
    "distance_km",
    "fuel_consumed_liters",
    "fuel_efficiency_kmpl",
    "traffic_level",
    "delivery_delay_minutes",
    "maintenance_cost",
    "fuel_cost",
    "total_trip_cost",
    "cost_per_km",
    "driver_performance_score"
]

master = master[final_columns]

# 6. SAVE MASTER TABLE
master.to_csv("data/processed/master_transportation_analytics.csv", index=False)

print("Master analytics table created successfully!")
