import pandas as pd
from cleaner import clean_data
from visualize_data import visualize_data
from roles import Intern, HR, Admin
from logger import Logger

df = pd.read_csv("data/messy_data.csv")

cleaned_df, log = clean_data(df)
print("Summary after cleaning:")
print(cleaned_df.info())
print(cleaned_df.describe())



Logger("logs/intern.log").log("Intern accessed cleaned data.")
Logger("logs/hr.log").log("HR reviewed hiring date consistency.")
Logger("logs/admin.log").log("Admin reviewed system activity.")

visualize_data(cleaned_df)
