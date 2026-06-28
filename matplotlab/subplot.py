# subplot 
import matplotlib.pyplot as plt
import pandas as pd 
df = pd.read_excel("Covid dataset.xlsx")
# subplot
figure, axes = plt.subplots(1,2, figsize = (8,4))
Age_quatile = df["Patient age quantile"]
Hemoglobin = df["Hemoglobin"]
# left subplot
axes[0].hist(Age_quatile, color = "red", bins = 15, edgecolor = "green") 
axes[0].set_xlabel("Age", color = "black", fontsize = 14, fontstyle = "normal")
axes[0].set_ylabel("number of patients", color = "black", fontsize = 14, fontstyle = "normal")
axes[0].set_title("Patient age quantile",color = "darkblue", fontsize = 14, fontstyle = "italic")
axes[0].grid(True, alpha = 0.1, color ="black" )
# right subplot
axes[1].hist(Hemoglobin,color = "blue", bins = 15, edgecolor = "green")
axes[1].set_xlabel("Hemoglobin", color = "black", fontsize = 14, fontstyle = "normal")
axes[1].set_ylabel("number of patients", color = "black", fontsize = 14, fontstyle = "normal")
axes[1].set_title("Hemoglobin of patients data",color = "darkblue", fontsize = 14, fontstyle = "italic")
axes[1].grid(True, alpha = 0.1, color ="black" )
figure.suptitle("Covid data analysis", fontsize = 16)
plt.tight_layout()
plt.show()