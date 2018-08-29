import numpy as np
import pandas as pd

#Reading CSV file .... 2017 NFL Fantasy PPR results
df = pd.read_csv("nfl_2017_ppr.csv")

print("*"*60)
print("Head of the CSV...")
print(df.head())

data = df[["Player", "Avg"]]
print(data.head())
#print(df)
