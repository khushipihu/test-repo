import pandas as pd
df = pd.read_excel("student_data_100.xlsx")
print("Sample DataFrame:")
print(df)
print("Descriptive Statistics:")
print(df.describe())