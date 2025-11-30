import pandas as pd
data = {
    "Name" : ['Khushi', 'Pihu', 'Sapna', 'Misti', 'Ankit', 'Rohan', 'Sonia', 'Amit', 'Neha', 'Vikram'],
    "Age" : [19, 18, 22, 10, 21, 23, 20, 22, 19, 24],
    "Salary" : [50000, 60000, 55000, 30000, 70000, 65000, 48000, 72000, 52000, 68000]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print("--" * 40)

df.sort_values(by=["Age"], ascending=True, inplace=True)
print("DataFrame sorted by Age in ascending order:")
print(df)

print("--" * 40)
df.sort_values(by=["Salary"], ascending=True, inplace=True)
print("DataFrame sorted by Salary in ascending order:")
print(df)