import pandas as pd
import matplotlib.pyplot as plt

def visualize_data(input_path, output_path):
    """
    Generate visualizations from cleaned data
    """
    df = pd.read_csv(input_path)
 
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    
    if len(numeric_cols) >= 2:
        plt.figure(figsize=(10, 6))
        plt.scatter(df[numeric_cols[0]], df[numeric_cols[1]])
        plt.title(f'{numeric_cols[0]} vs {numeric_cols[1]}')
        plt.xlabel(numeric_cols[0])
        plt.ylabel(numeric_cols[1])
        plt.grid(True)
        plt.savefig(output_path)
        plt.close()
    else:
        print("Not enough numeric columns for visualization")

    return df