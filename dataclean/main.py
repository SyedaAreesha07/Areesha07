import pandas as pd
from cleaner import clean_data

df = pd.read_csv("data/messy_data.csv")

cleaned_df, log = clean_data(df)

with open("output/clean_log.txt", "w") as f:
    f.write(log)

cleaned_df.to_csv("output/cleaned_data.csv", index=False)

print("Summary after cleaning:")
print(cleaned_df.info())
print(cleaned_df.describe())
