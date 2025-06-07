import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime
import pandas as pd

def visualize_data(df):
    os.makedirs("plots", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
   
    plt.figure(figsize=(8, 5))
    df['name'].value_counts().plot(kind='bar', title='Name Frequency')
    plt.xlabel("Name")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(f"plots/bar_plot_{timestamp}.png")
    plt.close()
    
    plt.figure(figsize=(8, 5))
    df_sorted = df.sort_values("joining_date")
    df_sorted['salary'] = pd.to_numeric(df_sorted['salary'], errors='coerce')
    plt.plot(df_sorted['joining_date'], df_sorted['salary'], marker='o')
    plt.title("Salary Trend Over Time")
    plt.xlabel("Joining Date")
    plt.ylabel("Salary")
    plt.tight_layout()
    plt.savefig(f"plots/line_plot_{timestamp}.png")
    plt.close()
    
    plt.figure(figsize=(8, 5))
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df['age'].dropna().plot(kind='hist', bins=10, title="Age Distribution")
    plt.xlabel("Age")
    plt.tight_layout()
    plt.savefig(f"plots/histogram_{timestamp}.png")
    plt.close()

    plt.figure(figsize=(8, 5))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(f"plots/heatmap_{timestamp}.png")
    plt.close()
    
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df['age'])
    plt.title("Age Outlier Detection")
    plt.tight_layout()
    plt.savefig(f"plots/boxplot_{timestamp}.png")
    plt.close()

    print(f"✅ Plots saved in 'plots/' folder with timestamp {timestamp}")
