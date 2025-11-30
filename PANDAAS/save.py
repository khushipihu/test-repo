import pandas as pd

data = {
    "Name" : ['Khushi', 'Pihu', 'Sapna', 'Misti'],
    "Age" : [19, 18, 22, 10],
    "City" : ['Delhi', 'Mumbai', 'Dhanbad', 'Kolkata']
}

df = pd.DataFrame(data)
print(df)

#df.to_csv("output.csv", index=False)
#df.to_excel("outtputt.xlsx", index = False)
df.to_json("output.json", index = False)
print("--"*40)
print("display first two rows")
print(df.head(2))