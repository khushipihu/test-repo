import pandas as pd
df = pd.read_excel("student_data_100.xlsx")
#df.to_csv("student.csv", index=False)
#df.to_json("student.json", index=False)
#df.to_excel("student_data_100.xlsx", index=False)
print("Displaying the information of the dataset")
print(df.info())