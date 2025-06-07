import pandas as pd

def clean_data(df):
    log = ""
    original_shape = df.shape

    missing_info = df.isnull().sum()
    log += "Missing values per column:\n" + str(missing_info) + "\n\n"

    for col in df.columns:
        if 'date' in col.lower():
            try:
                df[col] = pd.to_datetime(df[col], errors='coerce')
                log += f"Converted {col} to datetime.\n"
            except Exception as e:
                log += f"Failed to convert {col}: {e}\n"
    
    threshold = 0.5
    for col in df.columns:
        missing_ratio = df[col].isnull().mean()
        if missing_ratio > threshold:
            df.drop(columns=[col], inplace=True)
            log += f"Dropped column {col} (>{threshold*100}% missing).\n"
        else:
            if df[col].dtype == 'O':
                df[col].fillna("unknown", inplace=True)
                log += f"Filled missing in {col} with 'unknown'.\n"
            else:
                df[col].fillna(df[col].median(), inplace=True)
                log += f"Filled missing in {col} with median.\n"

    cleaned_df = df.dropna()
    log += f"\nDropped rows with remaining NaNs. New shape: {cleaned_df.shape}\n"

    log += f"\nOriginal shape: {original_shape} -> Cleaned shape: {cleaned_df.shape}\n"

    return cleaned_df, log
