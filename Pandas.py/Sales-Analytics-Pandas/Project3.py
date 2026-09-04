import pandas as pd
df = pd.read_csv("sales-data.csv")
"""
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
"""
df["Date"] = pd.to_datetime(df["Date"])
#print(df.info("Date"))

#Adding new columns
df["Revenue"] = df["Units_Sold"] * df["Unit_Price"]
df["Cost"] = df["Units_Sold"] * df["Cost_Price"]
df["Profit"] = df["Revenue"] - df["Cost"]
#print(df.head())
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
"""
# pivot tables
pivot_table = pd.pivot_table(df, index="Category", values="Revenue", columns="Region", aggfunc="sum")
print(pivot_table)
pivot_table2 = pd.pivot_table(df, index="Month", values="Revenue", columns="Category", aggfunc="sum")
print(pivot_table2)
df = df.sort_values(by="Date")
df = df.sort_values(by="Revenue", ascending=False)
df = df.sort_values(by="Profit", ascending=False)
print(df.head())
print(df.tail())

# Boolean Filtering
print(df[(df["Revenue"] > 100000) & (df["Profit"] > 20000)])
# Query Method
print(df.query("Revenue > 100000"))
"""

# Performance Analysis
df["Performance"] = df["Profit"].apply(lambda x: "High" if x >= 30000 else "Medium" if x >= 15000 else "Low")
"""
print(df[["Product", "Profit", "Performance"]].head())
print(df["Performance"].value_counts())
print(df.groupby("Category").agg({
    "Revenue": "mean",
    "Profit": "mean",
    "Units_Sold": "sum"
}))
print("Most Revenue-Generating, Profitable, and High-Volume Category:", df.groupby("Category").agg({"Revenue": "sum", "Profit": "sum", "Units_Sold": "sum"}).idxmax())
print("Least Revenue-Generating, Profitable, and High-Volume Category:", df.groupby("Category").agg({"Revenue": "sum", "Profit": "sum", "Units_Sold": "sum"}).idxmin())
"""


# Product DataFrame
product_info = pd.DataFrame({
    "Product": ["Laptop", "Headphones", "Office Chair", "Desk", "Monitor",
                "Keyboard", "Notebook", "Printer", "Pen Pack", "Bookshelf",
                "Mouse", "Whiteboard", "Tablet", "Cabinet", "Calculator",
                "Projector", "Study Table", "Markers", "USB Drive", "Lamp"],
    
    "Supplier": ["Dell", "Sony", "Ikea", "Ikea", "Samsung",
                 "Logitech", "Classmate", "HP", "Cello", "Ikea",
                 "Logitech", "Amazon Basics", "Samsung", "Godrej", "Casio",
                 "Epson", "Ikea", "Camlin", "SanDisk", "Philips"],
    
    "Rating": [4.5, 4.3, 4.2, 4.1, 4.4,
               4.6, 4.0, 4.2, 4.1, 4.3,
               4.5, 4.0, 4.6, 4.2, 4.7,
               4.1, 4.4, 4.0, 4.5, 4.2]
})
df = pd.merge(df, product_info, on="Product", how="left")
#highest average rated product
print("Highest Average Rated Product:", df.groupby("Supplier")["Rating"].mean().idxmax())
print("Lowest Average Rated Product:", df.groupby("Supplier")["Rating"].mean().idxmin())
print("Highest Revenue Supplier:", df.groupby("Supplier")["Revenue"].sum().idxmax())
print("Lowest Revenue Supplier:", df.groupby("Supplier")["Revenue"].sum().idxmin())
print("Total Revenue for each Supplier within each Category:", df.groupby(["Supplier", "Category"])["Revenue"].sum())
print("Highest average product rating for each category:", df.groupby("Category")["Rating"].mean().idxmax())
pivot_table3 = pd.pivot_table(df, index="Region", values=["Revenue", "Profit"], aggfunc="sum")
print(pivot_table3)
pivot_table4 = pd.pivot_table(df, index="Region", values="Profit", columns="Category", aggfunc="sum", fill_value=0)
print(pivot_table4)

df = df.rename(columns={"Units_Sold": "Quantity Sold", "Unit_Price": "Selling Price", "Cost_Price": "Purchase Price"})
print(df.head())
df = df.drop(columns=["Quantity Sold", "Purchase Price"])
print(df.head())