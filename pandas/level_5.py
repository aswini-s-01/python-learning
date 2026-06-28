# sorting 
import pandas as pd 
df = pd.read_excel("covid dataset.xlsx")
# hemoglobin in decending order
print(df.columns)
sort_df = df.sort_values(by="Hemoglobin", ascending = False)
print(sort_df[["Patient ID", "Hemoglobin"]])
# platelets in ascending order
sorted_df = df.sort_values(by="Platelets", ascending = True)
print(sorted_df[["Patient ID", "Platelets"]].head(10))
# statistics
Avg_hemoglobin = df["Hemoglobin"].mean()
Avg_Platelets = df["Platelets"].mean()
Avg_Leukocytes = df["Leukocytes"].mean()
print("The average value of hemoglobin:", Avg_hemoglobin)
print("The average value of Platelets:", Avg_Platelets)
print("The average value of Leukocytes:", Avg_Leukocytes)
# Maximum value of hemoglobin
Max_Hemoglobin = df["Hemoglobin"].max()
print("The maximum value of hemoglobin:", Max_Hemoglobin)
Min_Platelets = df["Platelets"].min()
print("The minimum value of platelets:", Min_Platelets)
# Group by 
# average hemoglobin
group_hem = df.groupby("SARS-Cov-2 exam result")["Hemoglobin"].mean()
print(group_hem)
group_platelets = df.groupby("SARS-Cov-2 exam result")["Platelets"].mean()
print(group_platelets)
# count by 
print(df["SARS-Cov-2 exam result"].value_counts())
# total no of patients 
Total_patients = len(df) 
print("The total no of patients:", Total_patients)
# total covid positive patients 
print((df["SARS-Cov-2 exam result"] == "positive").sum()) # or 
Positive = (df["SARS-Cov-2 exam result"].value_counts() ["positive"])
print("The no_positive case:", Positive)
print(df["SARS-Cov-2 exam result"].value_counts() ["negative"])
# percentage of positive patients 
positive_percentage = (Positive / Total_patients)*100
print("The percentage of positive cases:", positive_percentage)
# number of patients admitted in icu 
print(df["Patient addmited to intensive care unit (1=yes, 0=no)"].value_counts()[1])# or 
print((df["Patient addmited to intensive care unit (1=yes, 0=no)"] == 1).sum() )
print((df["Patient addmited to regular ward (1=yes, 0=no)"] == 1).sum())
#Average Hemoglobin of COVID positive patients
Avg_hem =df[df["SARS-Cov-2 exam result"] == "positive"]["Hemoglobin"].mean()
print(Avg_hem)
#Average Platelets of COVID positive patients
Avg_Platelets_positive = df[df["SARS-Cov-2 exam result"] == "positive"]["Platelets"].mean()
print(Avg_Platelets_positive)