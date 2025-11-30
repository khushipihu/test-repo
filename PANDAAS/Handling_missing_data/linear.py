import pandas as pd
data = {
    "Time" : [1, 2, 3, 4, 5],
    "Value" : [10, None, 30, None, 50]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print('--'*40)

df['Value'].interpolate(method='linear', inplace=True)
print("DataFrame after Linear Interpolation:")  
print(df)