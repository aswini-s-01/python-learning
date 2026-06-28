import matplotlib.pyplot as plt
import pandas as pd 
df = pd.read_excel("Covid dataset.xlsx")
# histrogram 
age = df["Patient age quantile"]
plt.hist(age, bins = 20)
plt.xlabel("age")
plt.ylabel("Number of patients")
plt.title("Patient age quantile")
plt.show()
# count total number of positive and negative cases
count = df["SARS-Cov-2 exam result"].value_counts()
plt.bar(count.index, count.values)
plt.xlabel("Results")
plt.ylabel("count")
plt.title("Result of covid test")
plt.show()