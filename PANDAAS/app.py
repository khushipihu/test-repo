import pandas as pd
df = pd.read_excel("student_data_100.xlsx")
print("Printing first 10 rows")
print(df.head(10))

print("--"*40)
print("Displaying last 10 rows")
print(df.tail(10))