import pandas as pd 
df = pd.read_excel("covid dataset.xlsx")
# column selection 
print(df.columns)
# To check the column 
print (df[["Patient ID", "SARS-Cov-2 exam result"]])
print(df[["Hemoglobin", "Platelets", "Leukocytes"]])
# first twnty values of sars cov 2
print(df["SARS-Cov-2 exam result"].head(20))
