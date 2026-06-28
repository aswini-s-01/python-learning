import pandas as pd
df = pd.read_excel("covid dataset.xlsx")
# data clearning
print(df.isnull().sum())
# sort the missing value
print(df.isnull().sum().sort_values(ascending=False))
# to check the dulpicate row exist
print(df.duplicated().sum())
# remove the duplicate and store 
df_clean = df.drop_duplicates()
print(df_clean.shape)

