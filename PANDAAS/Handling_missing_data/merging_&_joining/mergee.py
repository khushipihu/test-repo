import pandas as pd
df_coustomers = pd.DataFrame({
    "Name" : ['Khushi', 'Pihu', 'Sapna', 'Misti', 'Ankit', 'Rohan', 'Sonia', 'Amit', 'Neha', 'Vikram'],
    "Age" : [19, 18, 22, 10, 21, 23, 20, 22, 19, 24],
    "Salary" : [50000, 60000, 55000, 30000, 70000, 65000, 48000, 72000, 52000, 68000],
    "Employee_ID": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
})

df_orders = pd.DataFrame({
    "Employee_ID": [10, 30, 40, 50, 60, 70, 80, 90, 100, 110],
    "Order_Amount": [250, 300, 150, 400, 500, 350, 450, 600, 200, 550]
})

# Merging the two DataFrames on 'Employee_ID'

#df_merged = pd.merge(df_coustomers, df_orders, on='Employee_ID', how='inner')
#df_merged = pd.merge(df_coustomers, df_orders, on='Employee_ID', how='outer')
#df_merged = pd.merge(df_coustomers, df_orders, on='Employee_ID', how='left')
df_merged = pd.merge(df_coustomers, df_orders, on='Employee_ID', how='right')
print(df_merged)

print('--'*40)
