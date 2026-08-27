import pandas as pd
Data = {
    "Name":["Shiv", "Nove", "Git"],
    "Age":[23, 21, 20],
    "Course":["MPCS", "MAICS", "MSCS"]
}
df = pd.DataFrame(Data, index=["Student1", "Student2", "Student3"])
df["Marks"] = [56, 76, 88]
#new rows
new_row = pd.DataFrame([{"Name":"Mari","Age":19,"Course":"BBA","Marks":78},
                       {"Name":"Heru","Age":21,"Course":"Bcom","Marks":88}],index=["Student4", "Student5"])
df = pd.concat([df,new_row])
#Filtering
print(df[df["Marks"] >= 80])
print(df[df["Age"] <= 22])
print(df[df["Course"] == "MAICS"])
print(df[(df["Marks"] <= 70) & (df["Marks"] <= 90)])
print(df[(df["Course"] == "MAICS") | (df["Course"] == "MPCS")])

# Sorting Data
print(df.sort_values(by=['Marks']))
print(df.sort_values(by=['Marks'],ascending=False))
print(df.sort_values(by=['Age','Marks']))
print(df.sort_values(by=['Name']))
df = df.sort_values(by=['Marks'],ascending=False)
print(df.iloc[0:3])

#Data Cleaning
student_data = {
    "Name": ["Shiv", "Nove", "Git", "Alex", "Ram", "John", "Sara"],
    "Age": [21, 20, None, 22, 21, None, 23],
    "Course": ["MAICS", "MPCS", "MSCS", None, "MAICS", "MPCS", None],
    "Marks": [89, None, 76, 95, None, 68, 84],
    "Attendance": [92, 88, None, 96, 85, None, 90]
}

df2 = pd.DataFrame(student_data)
print(df2.isnull())
print(df2.isnull().sum())
print(df2.isnull().sum().sum())
print(df2.isnull().mean().multiply(100))
df_clean = df2.dropna()
print(df_clean)
df2["Marks"] = df2["Marks"].fillna(df2["Marks"].mean())
df2["Age"] = df2["Age"].fillna(df2['Age'].median())
df2["Course"] = df2["Course"].fillna("Unknown")
df2["Attendance"] = df2["Attendance"].fillna(0)
print(df2)

#Duplicates
data2 = {
    "Name": ["Shiv", "Nove", "Git", "Alex", "Shiv", "Git", "Sara"],
    "Course": ["MAICS", "MPCS", "MSCS", "MAICS", "MAICS", "MSCS", "MPCS"],
    "Marks": [89, 76, 82, 95, 89, 82, 91]
}

df3 = pd.DataFrame(data2)
print(df3)
print(df3.duplicated())
print(df3.duplicated().sum())
df3_delete_duplicates = df3.drop_duplicates().reset_index()
print(df3_delete_duplicates)

