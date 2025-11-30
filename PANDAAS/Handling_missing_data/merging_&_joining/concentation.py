import pandas as pd
df_Region1 = pd.DataFrame({
    'Customer_ID': [1, 2, 3, 4, 5],
    'Name': ['Anaya', 'Bistt', 'Chandni', 'Divya', 'Shruti']
})

df_Region2 = pd.DataFrame({
    'Customer_ID': [6, 7, 8, 9, 10],
    'Name': ['Esha', 'Fiona', 'Gauri', 'Hina', 'Isha']
})
# Concatenating the two DataFrames along rows

df_concat = pd.concat([df_Region1, df_Region2], axis = 0, ignore_index=True)
print(df_concat)