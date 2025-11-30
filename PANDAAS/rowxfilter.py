import pandas as pd
data = {
    "Name" : ['Khushi', 'Pihu', 'Sapna', 'Misti', 'Ankit', 'Rohan', 'Sonia', 'Amit', 'Neha', 'Vikram'],
    "Age" : [19, 18, 22, 10, 21, 23, 20, 22, 19, 24],
    "Salary" : [50000, 60000, 55000, 30000, 70000, 65000, 48000, 72000, 52000, 68000],
    "Performance_Score" : [85, 90, 88, 70, 92, 87, 80, 95, 83, 89]
}
df = pd.DataFrame(data)

high_salary = df[df['Salary']>50000]
print("Employees with Salary greater than 50000:")
print(high_salary)
print("\n")
filtered = df[(df['Age']>20)& (df['Salary']>60000)]
print("Names of Employees with Age greater than 20 and with salary greater than 60000:")
print(filtered)