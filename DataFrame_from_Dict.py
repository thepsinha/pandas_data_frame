import pandas as pd
df = pd.DataFrame()
Stu_name = ["IShani","Ayaan","Cije","Sid","Sam","Rehaan","Dev"]
age = [23,25,28,26,27,24,30]

data = {"Student_name":Stu_name,"Age":age}
df = pd.DataFrame(data)
print(df)
