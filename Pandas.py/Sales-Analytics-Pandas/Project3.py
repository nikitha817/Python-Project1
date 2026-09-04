import pandas as pd
df = pd.read_csv("sales-data.csv")
"""
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
"""
df["Date"] = pd.to_datetime(df["Date"])
print(df.info("Date"))

#Adding new columns
df["Revenue"] = df["Units_Sold"] * df["Unit_Price"]
df["Cost"] = df["Units_Sold"] * df["Cost_Price"]
df["Profit"] = df["Revenue"] - df["Cost"]
print(df.head())
"""
#Total Revenue, Cost and Profit
print("Total Revenue:", df["Revenue"].sum())
print("Total Cost:", df["Cost"].sum())
print("Total Profit:", df["Profit"].sum())

#best Profitable product
print("Best Performing Product:", df.groupby("Product")["Profit"].sum().idxmax())
#best selling product
print("Best Selling Product:", df.groupby("Product")["Units_Sold"].sum().idxmax())
#Worst selling product
print("Worst Selling Product:", df.groupby("Product")["Units_Sold"].sum().idxmin())

#Categorical Analysis
print("Revenue by Category:", df.groupby("Category")["Revenue"].sum())
print("Profit by Category:", df.groupby("Category")["Profit"].sum())
print("Region wise Revenue:", df.groupby("Region")["Revenue"].sum())
print("Highest Profitable Region:", df.groupby("Region")["Profit"].sum().idxmax())
"""
df["Month"] = df["Date"].dt.month_name()
"""
print(df[["Date", "Month"]].head())
print("Highest revenue month:", df.groupby("Month")["Revenue"].sum().idxmax())
print("Highest profit month:", df.groupby("Month")["Profit"].sum().idxmax())
print("Lowest revenue month:", df.groupby("Month")["Revenue"].sum().idxmin())
print("Lowest profit month:", df.groupby("Month")["Profit"].sum().idxmin())
"""
