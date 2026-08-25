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
data = {"Employee":"NaN",
        "Job":"Unemployed"}
df2 = pd.DataFrame(data)