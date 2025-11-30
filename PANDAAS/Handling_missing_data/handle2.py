import pandas as pd
data = {
    "Name" : ['Khushi', 'None', 'Sapna', None, 'Ankit', None, 'Sonia', 'Amit', 'Neha', 'Vikram'],
    "Age" : [19, 18, 22, 10, None, 23, 20, 22, 19, None],
    "Salary" : [50000, None, 55000, 30000, 70000, 65000, 48000, 72000, None, 68000],
    "Performance_Score" : [85, 90, None, 70, 92, None, 80, 95, None, 89]
}
df = pd.DataFrame(data)
print(df)
print('--'*40)

#df.fillna(0, inplace=True)
#print(df)

df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
df['Performance_Score'].fillna(df['Performance_Score'].mean(), inplace=True)
print(df)