import pandas as pd
data = {
    "Name" : ['Khushi', 'Pihu', 'Sapna', 'Misti', 'Ankit', 'Rohan', 'Sonia', 'Amit', 'Neha', 'Vikram'],
    "Age" : [19, 18, 22, 10, 21, 23, 20, 22, 19, 24],
    "Salary" : [50000, 60000, 55000, 30000, 70000, 65000, 48000, 72000, 52000, 68000],
    "Performance_Score" : [85, 90, 88, 70, 92, 87, 80, 95, 83, 89]
}
df = pd.DataFrame(data)
print(df)
print('--'*40)

#increasing salary by 5%
df['Salary'] = df['Salary']*1.05
print(df)