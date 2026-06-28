# customization plot 
import pandas as pd 
import matplotlib.pyplot as plt 
df = pd.read_excel("Covid dataset.xlsx")
# line plot 
age = df["Patient age quantile"].head(50)
plt.figure(figsize=(3,5))
plt.plot(age, marker = "*", markerfacecolor = "black", markeredgecolor ="red",
         linestyle = ":", color = "black", label = "ages")
plt.xlabel("number_of _patients", color = "black", fontstyle = "normal", fontsize= 14)
plt.ylabel("ages", color = "black", fontstyle = "normal", fontsize= 14)
plt.title("Patient age quantile", color = "black", fontstyle = "italic", fontsize= 14)
plt.grid(True, alpha = 0.5, color = "black")
plt.show() 