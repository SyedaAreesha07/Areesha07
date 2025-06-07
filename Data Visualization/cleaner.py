import pandas as pd

def clean_data(df):
    log = []

    for col in df.select_dtypes(include='object').columns:
        log.append(f"Filling missing values in '{col}' with 'unknown'")
        df[col] = df[col].fillna("unknown")

    for col in df.select_dtypes(include='number').columns:
        median = df[col].median()
        log.append(f"Filling missing numeric values in '{col}' with median={median}")
        df[col] = df[col].fillna(median)

    if 'joining_date' in df.columns:
        log.append("Converting 'joining_date' to datetime")
        df['joining_date'] = pd.to_datetime(df['joining_date'], errors='coerce')
   
    for col in ['age', 'salary']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    return df, log
