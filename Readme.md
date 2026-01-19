# Transportation Analytics Project

## Project Overview
The Transportation Analytics Project is a data-driven analysis system designed to evaluate transportation operations using real-world datasets. It analyzes fuel usage, vehicle efficiency, driver performance, route costs, delays, and maintenance data to generate insights, visualizations, and reports that support decision-making in logistics and transportation management.

---

## Objectives
- Analyze transportation and logistics data
- Measure vehicle fuel efficiency and operating costs
- Evaluate driver performance and delivery delays
- Generate analytical reports and dashboards
- Produce cleaned, merged datasets for further analysis

---

## Project Structure
Transportation_Analytics_Project/
│
├── analysis.py # Core data analysis logic
├── cost_analysis.py # Transportation cost calculations
├── create_csv_files.py # Generates CSV datasets
├── dashboard.py # Dashboard and visualization script
├── generate_report.py # Creates Excel and PDF reports
├── merge_data.py # Merges multiple datasets
├── summary.py # Generates summary statistics
│
├── data/
│ ├── raw/ # Original datasets
│ │ ├── drivers.csv
│ │ ├── fuel_logs.csv
│ │ ├── gps_routes.csv
│ │ ├── maintenance.csv
│ │ ├── trips.csv
│ │ └── vehicles.csv
│ │
│ └── processed/ # Cleaned and processed data
│ ├── master_transportation_analytics.csv
│ ├── summary_tables.xlsx
│ └── vehicle_efficiency_ranking.csv
│
├── reports/
│ ├── master_transportation_analytics.xlsx
│ └── transportation_report.pdf
│
├── visuals/
│ ├── correlation_heatmap.png
│ ├── cost_per_km_by_route.png
│ ├── delivery_delay_distribution.png
│ ├── driver_performance.png
│ └── fuel_efficiency_by_vehicle.png


---

##Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib / Seaborn
- OpenPyXL
- ReportLab (for PDF generation)

---

## How to Run the Project

1. **Clone or download the project**
2. Install required libraries:
   ```bash
   pip install pandas numpy matplotlib seaborn openpyxl reportlab


Generate CSV files:
python create_csv_files.py

Merge datasets:
python merge_data.py


Perform analysis:
python analysis.py
python cost_analysis.py
python summary.py


Generate reports and dashboards:
python generate_report.py
python dashboard.py

Outputs

Cleaned master dataset
Excel summary tables
PDF transportation report
Visual analytics (charts & heatmaps)

Future Enhancements

Add machine learning models for cost prediction
Real-time data ingestion
Web-based dashboard using Streamlit or Flask
Automated alerts for delays and high fuel consumption

Author
Poojitha Gollapudi

License
This project is for educational and academic use.