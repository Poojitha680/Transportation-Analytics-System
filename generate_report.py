import pandas as pd
from fpdf import FPDF
import os

#Load Data
master_csv = "data/processed/master_transportation_analytics.csv"
summary_excel = "data/processed/summary_tables.xlsx"

df_master = pd.read_csv(master_csv)
print("Master table loaded.")
print("Summary tables loaded from Excel.")

#Creating the PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", "B", 16)

pdf.cell(0, 10, "Transportation Analytics Report", ln=True, align="C")
pdf.ln(5)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 8, "This report summarizes insights from fleet transportation analytics, including fuel efficiency, route costing, delivery delays, vehicle and driver performance, and cost optimization strategies.")

#Add Summary Tables (Route Cost)
route_cost = pd.read_excel(summary_excel, sheet_name="Route Cost")
pdf.ln(5)
pdf.set_font("Arial", "B", 14)
pdf.cell(0, 10, "Average Cost per Km by Route Type", ln=True)
pdf.set_font("Arial", "", 12)

for i, row in route_cost.iterrows():
    pdf.cell(0, 8, f"{row['Route Type']}: {row['Average Cost per Km']:.2f}", ln=True)

# Adding Vehicle Efficiency Table
vehicle_eff = pd.read_excel(summary_excel, sheet_name="Vehicle Efficiency")
pdf.ln(5)
pdf.set_font("Arial", "B", 14)
pdf.cell(0, 10, "Vehicle Fuel Efficiency Ranking", ln=True)
pdf.set_font("Arial", "", 12)

for i, row in vehicle_eff.iterrows():
    pdf.cell(0, 8, f"{row['Vehicle ID']}: {row['Average Fuel Efficiency (Km/L)']:.2f}", ln=True)

#Embeding the created Visualizations
pdf.ln(5)
pdf.set_font("Arial", "B", 14)
pdf.cell(0, 10, "Visualizations", ln=True)

visuals = [
    "visuals/fuel_efficiency_by_vehicle.png",
    "visuals/delivery_delay_distribution.png",
    "visuals/cost_per_km_by_route.png",
    "visuals/driver_performance.png",
    "visuals/correlation_heatmap.png"
]

for v in visuals:
    if os.path.exists(v):
        pdf.ln(5)
        pdf.image(v, w=170)

#Save PDF
os.makedirs("reports", exist_ok=True)
pdf_file = "reports/transportation_report.pdf"
pdf.output(pdf_file)

print(f"PDF report saved: {pdf_file}")

# 7. Saving Master Table as Excel
excel_file = "reports/master_transportation_analytics.xlsx"
df_master.to_excel(excel_file, index=False)
print(f"Cleaned master table saved as Excel: {excel_file}")
