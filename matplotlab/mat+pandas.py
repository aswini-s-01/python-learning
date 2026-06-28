# matplot lab and pandas
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_excel("Covid dataset.xlsx")
#Mean hemoglobin for Positive patients
#Mean hemoglobin for Negative patients
mean_hemoglobin = df.groupby("SARS-Cov-2 exam result")["Hemoglobin"].mean()
print(mean_hemoglobin.index)
print(mean_hemoglobin.values)
plt.figure(figsize = (8,4))
plt.bar(mean_hemoglobin.index, mean_hemoglobin.values, color = "green", edgecolor = "red")
for i, val in enumerate(mean_hemoglobin.values):
    plt.text(i, val, round(val, 2), ha="center", va="bottom"  )
plt.xlabel("mean", color = "black", fontstyle = "italic",fontsize = 14)
plt.ylabel("hemoglobin", color = "black", fontstyle = "italic",fontsize = 14)
plt.title("Hemoglobin of covid positive and negative patients", color = "black", fontstyle = "normal",fontsize = 14)
plt.grid(axis="y", alpha=0.3)
plt.show()
# platelets
mean_platelets = df.groupby("Patient age quantile")["Platelets"].mean()
print(mean_platelets)
plt.figure(figsize = (8,4))
plt.bar(mean_platelets.index, mean_platelets.values, color = "blue",edgecolor = "darkblue")
for i, val in enumerate(mean_platelets.values):
    plt.text(i, val, round(val,2), ha='center', va='bottom')
plt.xlabel("age", color = "black", fontsize = 14, fontstyle = "normal")
plt.ylabel("platelets", color = "black", fontsize = 14, fontstyle = "normal")
plt.title("Avg_mean value of platelets for covid patient according to age", color = "blue", fontsize = 16, fontstyle = "italic")
plt.grid(axis = "y", alpha = 0.2)
plt.show()