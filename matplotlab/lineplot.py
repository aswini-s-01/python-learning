import matplotlib.pyplot as plt
import pandas as pd 
df = pd.read_excel("Covid dataset.xlsx")
#print(df.columns)
# line plot 
age = df["Patient age quantile"].head(50)
plt.plot(age)
plt.xlabel("Patient_numbers", fontsize = 12, color = "black", fontstyle = "italic")
plt.ylabel("age", fontsize = 12, color = "black", fontstyle = "italic")
plt.title("Patient age quantile", fontsize = 16, color = "black", fontstyle = "oblique")
plt.show()
# Exercise 2 (Scatter_plot)
clear_df = df[["Hemoglobin", "Platelets"]].dropna()
# scatter plots
plt.scatter(clear_df["Hemoglobin"], clear_df["Platelets"])
plt.xlabel("Hemoglobin", fontsize = 12, fontstyle = "normal", color = "Black")
plt.ylabel("Platelets", fontsize = 12, fontstyle = "normal", color = "Black")
plt.title("Scatter plot for Hemoglobin and platelets")
plt.show()
