import pandas as pd

# Vehicles dataset
vehicles = pd.DataFrame({
    "vehicle_id": ["V001","V002","V003","V004","V005"],
    "vehicle_type": ["Truck","Truck","Van","Truck","Van"],
    "manufacturer": ["Tata","Ashok Leyland","Mahindra","Eicher","Tata"],
    "model": ["Ace","Dost","Bolero Pickup","Pro 2049","Intra V30"],
    "year": [2019,2020,2018,2021,2022],
    "avg_mileage_kmpl": [14,13,15,12,16]
})

# Drivers dataset
drivers = pd.DataFrame({
    "driver_id": ["D001","D002","D003","D004","D005"],
    "driver_name": ["Ramesh Kumar","Suresh Patel","Anil Sharma","Vikram Singh","Manoj Das"],
    "age": [34,41,29,38,26],
    "experience_years": [8,15,5,12,3],
    "license_type": ["Heavy","Heavy","Light","Heavy","Light"]
})

# Trips dataset
trips = pd.DataFrame({
    "trip_id": ["T001","T002","T003","T004","T005"],
    "vehicle_id": ["V001","V002","V003","V004","V005"],
    "driver_id": ["D001","D002","D003","D004","D005"],
    "trip_date": ["2025-12-01","2025-12-01","2025-12-02","2025-12-02","2025-12-03"],
    "route_type": ["City","Highway","Rural","City","Highway"],
    "distance_km": [120,300,180,90,250],
    "traffic_level": ["High","Medium","Low","High","Medium"],
    "route_difficulty": [4,2,3,4,2]
})

# Fuel logs
fuel_logs = pd.DataFrame({
    "trip_id": ["T001","T002","T003","T004","T005"],
    "fuel_consumed_liters": [10,22,12,9,15],
    "fuel_cost_per_liter": [98,97,96,99,97]
})

# GPS routes
gps_routes = pd.DataFrame({
    "trip_id": ["T001","T002","T003","T004","T005"],
    "avg_speed_kmph": [35,65,45,30,70],
    "delivery_delay_minutes": [25,5,10,30,0]
})

# Maintenance dataset
maintenance = pd.DataFrame({
    "vehicle_id": ["V001","V002","V003","V004","V005"],
    "maintenance_date": ["2025-11-15","2025-11-20","2025-11-18","2025-11-25","2025-11-30"],
    "maintenance_cost": [4500,3000,2500,5200,2000]
})

# Save CSV files into data/raw folder
vehicles.to_csv("data/raw/vehicles.csv", index=False)
drivers.to_csv("data/raw/drivers.csv", index=False)
trips.to_csv("data/raw/trips.csv", index=False)
fuel_logs.to_csv("data/raw/fuel_logs.csv", index=False)
gps_routes.to_csv("data/raw/gps_routes.csv", index=False)
maintenance.to_csv("data/raw/maintenance.csv", index=False)

print("CSV files created successfully inside data/raw/")
