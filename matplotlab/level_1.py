import matplotlib.pyplot as plt
import pandas as pd 
#  Exercise 1
age = [10,20,30,40,50]
patients = [5,10,20,15,8]
plt.plot(age, patients)
plt.xlabel("age")
plt.ylabel("patient_count")
plt.title("Patients by Age")
plt.show()
# exercise 2
df = pd.read_excel("covid dataset.xlsx")
print(df.columns)
# Patient age quantile
ages = df["Patient age quantile"].head(10)
plt.plot(ages)
plt.xlabel("Patient Number")
plt.ylabel("age Quantile")
plt.title("Age Qantile of first 100 patients")
plt.show()
# Bar chart 
counts = df["SARS-Cov-2 exam result"].value_counts()
plt.bar(counts.index, counts.values)
plt.title("COVID Test Results")
plt.xlabel("Results")
plt.ylabel("count")
plt.show()
