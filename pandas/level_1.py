import pandas as pd 
df = pd.read_excel("covid dataset.xlsx")
print(df.head(10))
#no_of_rows
print(df.shape)
#no_of_column
print(df.columns)
#null value
df.info()
# describe
print(df.describe())



