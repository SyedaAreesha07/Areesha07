import os
import sys
from datetime import datetime
from clean_data import clean_data
from visualize_data import visualize_data
from generate_report import generate_report

def main():
 
    os.makedirs('data', exist_ok=True)
    os.makedirs('reports', exist_ok=True)
    os.makedirs('visualizations', exist_ok=True)
    
    raw_data_path = 'data/raw_data.csv'
    cleaned_data_path = 'data/cleaned_data.csv'
    visualization_path = 'visualizations/data_visualization.png'
    report_csv_path = 'reports/summary_report.csv'
    report_txt_path = 'reports/summary_report.txt'
    
    print("Starting data processing pipeline...")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    print("\nStep 1: Cleaning data...")
    clean_data(raw_data_path, cleaned_data_path)
    
    print("\nStep 2: Visualizing data...")
    visualize_data(cleaned_data_path, visualization_path)
    
    print("\nStep 3: Generating reports...")
    generate_report(cleaned_data_path, report_csv_path, report_txt_path)
    
    print("\nPipeline completed successfully!")

if __name__ == "__main__":
    main()