import pandas as pd
from datetime import datetime

def generate_report(input_path, csv_output_path, txt_output_path):
   
    df = pd.read_csv(input_path)
 
    summary = df.describe(include='all').round(2)
    summary.loc['count'] = df.count()
    summary.loc['unique'] = df.nunique()
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    file_info = f"Data file: {input_path}\nRecords: {len(df)}\nColumns: {len(df.columns)}"
 
    summary.to_csv(csv_output_path)

    with open(txt_output_path, 'w') as f:
        f.write(f"DATA SUMMARY REPORT\n")
        f.write(f"Generated at: {timestamp}\n\n")
        f.write(f"{file_info}\n\n")
        f.write("SUMMARY STATISTICS:\n")
        f.write(summary.to_string())
        f.write("\n\nCOLUMN DETAILS:\n")
        for col in df.columns:
            f.write(f"\n{col}:\n")
            if df[col].dtype in ['float64', 'int64']:
                f.write(f"  Mean: {df[col].mean():.2f}\n")
                f.write(f"  Median: {df[col].median():.2f}\n")
                f.write(f"  Std Dev: {df[col].std():.2f}\n")
            else:
                f.write(f"  Type: {df[col].dtype}\n")
                f.write(f"  Unique values: {df[col].nunique()}\n")
                f.write(f"  Most common: {df[col].mode().values[0]}\n")
    
    return summary