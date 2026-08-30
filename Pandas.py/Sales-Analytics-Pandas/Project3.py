import pandas as pd
df = pd.read_csv("sales-data.csv")

print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
df["Date"] = pd.to_datetime(df["Date"])
print(df.info("Date"))