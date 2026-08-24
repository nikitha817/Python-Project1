import pandas as pd
df = pd.DataFrame({
    "Name":["Shiv", "Nove", "Git"],
    "Age":[23, 21, 20],
    "Course":["MPCS", "MAICS", "MSCS"]
}, index=["Student1","Student2","Student3"])
df["Marks"] = [56, 76, 88]
#new rows
new_row = pd.DataFrame([{"Name":"Mari","Age":19,"Course":"BBA","Marks":78},
                       {"Name":"Heru","Age":21,"Course":"Bcom","Marks":88}],index=["Student4", "Student5"])
df =pd.concat([df,new_row])
print(df)