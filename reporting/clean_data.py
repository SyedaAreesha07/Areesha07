import pandas as pd
import numpy as np

def clean_data(input_path, output_path):

    df = pd.read_csv(input_path)
    
    df = df.drop_duplicates()

    for col in df.select_dtypes(include=[np.number]).columns:
        df[col] = df[col].fillna(df[col].median())

    date_columns = df.select_dtypes(include=['object']).columns[df.select_dtypes(include=['object']).apply(lambda x: x.str.contains('/|-').any())]
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')

    df.to_csv(output_path, index=False)
    return df