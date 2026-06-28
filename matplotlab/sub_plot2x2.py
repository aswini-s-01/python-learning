import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_excel("Covid dataset.xlsx")
# subplot 2x2 matrix 
figures,axes = plt.subplots(2,2, figsize = (12,8))
age = df["Patient age quantile"]
Hemoglobin = df["Hemoglobin"]
Platelets = df["Platelets"]
clear_df = df[["Hemoglobin", "Platelets"]].dropna()
# left upper corner[0,0]
axes[0,0].hist(age, bins = 13, color = "black", edgecolor = "red")
axes[0,0].set_xlabel("ages", color = "black", fontsize = 12, fontstyle = "normal")
axes[0,0].set_ylabel("Number of patients", color = "black", fontsize = 12, fontstyle = "normal")
axes[0,0].set_title("Age of the patients", color = "black", fontsize = 14, fontstyle = "italic")
axes[0,0].grid(True, alpha = 0.1, color = "grey")
# right upper corner[0,1]
axes[0,1].hist(Hemoglobin.dropna(), bins = 13, color = "darkblue", edgecolor = "red")
axes[0,1].set_xlabel("Hemoglobin", color = "black", fontsize = 12, fontstyle = "normal")
axes[0,1].set_ylabel("Number of patients", color = "black", fontsize = 12, fontstyle = "normal")
axes[0,1].set_title("Hemoglobin of the patients", color = "black", fontsize = 14, fontstyle = "italic")
axes[0,1].grid(True, alpha = 0.1, color = "brown")
#left lower corner[1,0]
axes[1,0].hist(Platelets.dropna(), bins = 13, color = "lightblue", edgecolor = "red")
axes[1,0].set_xlabel("Platelets", color = "black", fontsize = 12, fontstyle = "normal")
axes[1,0].set_ylabel("Number of patients", color = "black", fontsize = 12, fontstyle = "normal")
axes[1,0].set_title("Platelets of the patients", color = "black", fontsize = 14, fontstyle = "italic")
axes[1,0].grid(True, alpha = 0.1, color = "black")
# right lower corner[1,1]
axes[1,1].scatter(clear_df["Hemoglobin"], clear_df["Platelets"])
axes[1,1].set_xlabel("Hemoglobin", color = "black", fontsize = 12, fontstyle = "normal")
axes[1,1].set_ylabel("Platelets", color = "black", fontsize = 12, fontstyle = "normal")
axes[1,1].set_title("Platelets vs Hemoglobin", color = "black", fontsize = 14, fontstyle = "italic")
plt.suptitle("COVID Dataset Exploratory Analysis", color = "black", fontsize = 16, fontstyle = "italic")
plt.tight_layout()
plt.show()

