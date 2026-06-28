# Dataset Exploration
import pandas as pd 
df = pd.read_excel("Covid dataset.xlsx")
print(df.head)
print(df.shape)
print(df.columns)
df. info()
print(df.describe())
# Find the number of missing values in each column
print(df.isnull().sum())
# Display the top 10 columns with the highest missing values.
print(df.isnull().sum().sort_values(ascending = False).head(10))
print(df.duplicated().sum())
df_clean = df.drop_duplicates()
print(df_clean.shape)
# column selection
print(df[["Patient ID" , "SARS-Cov-2 exam result"]])
print(df[["Hemoglobin", "Platelets", "Leukocytes"]])
print(df["SARS-Cov-2 exam result"].head(20))
# filtering 
print(df[df["SARS-Cov-2 exam result"] == "positive"])
print(df[df["SARS-Cov-2 exam result"] == "negative"])
print(df[df["Patient addmited to intensive care unit (1=yes, 0=no)"] == 1][["Patient addmited to intensive care unit (1=yes, 0=no)"]])
# covid postive patient + admitted in icu
print(
    df[(df["Patient addmited to intensive care unit (1=yes, 0=no)"] == 1) &
       (df["SARS-Cov-2 exam result"] == "positive")]
[["Patient addmited to intensive care unit (1=yes, 0=no)", "SARS-Cov-2 exam result"]] )
#age is > 15
print(df[df["Patient age quantile"] > 15 ])
# age > 15 and covid positive 
print(
    df[(df["Patient age quantile"] > 15) & 
       (df["SARS-Cov-2 exam result"] == "positive")]
       [["Patient age quantile", "SARS-Cov-2 exam result"]]
)
# sorting
sorted_df = df.sort_values(by="Hemoglobin", ascending = False)
print(sorted_df[["Patient ID", "Hemoglobin"]])
print(df.sort_values(by="Platelets", ascending = True) [["Platelets"]])
sort_platelets = df.sort_values(by="Platelets", ascending = False)
print(sort_platelets[["Patient ID","Platelets"]])
# Statistics
Avg_hem = df["Hemoglobin"].mean()
Avg_platelets = df["Platelets"].mean()
Avg_leukocytes = df["Leukocytes"].mean()
print("The Avg_hemoglobin:", Avg_hem)
print("The Avg_platelets:", Avg_platelets)
print("The Avg_leukocytes:", Avg_leukocytes)
# maximum 
max_hemoglobin = df["Hemoglobin"].max()
print("The maximum hemoglobin:", max_hemoglobin)
min_platelets = df["Platelets"].min()
print("The minimum platelets:", min_platelets)
# group by
group_hem = df.groupby("SARS-Cov-2 exam result")["Hemoglobin"].mean()
print("The average Hemoglobin grouped by COVID result:", group_hem)
group_platelets = df.groupby("SARS-Cov-2 exam result")["Platelets"].mean()
print("The average platelets grouped by COVID result:", group_platelets)
# counts and percentage 
# value_count
print(df["SARS-Cov-2 exam result"].value_counts())
total_patient = len(df)
print("The total patient:", total_patient)
total_covid_patient = (df["SARS-Cov-2 exam result"] == "positive").sum()
print("The total covid positive patients:", total_covid_patient)
total_covidn_patient = (df["SARS-Cov-2 exam result"] == "negative").sum()
print("Total covid negative patients:", total_covidn_patient)
#percentage to check covid positive and negative patient 
percentage = df["SARS-Cov-2 exam result"].value_counts(normalize = True) *100
print("The percentage of covid positve and negative patients are:", percentage)
# how many pate]ients where admitted to icu
print(df["Patient addmited to intensive care unit (1=yes, 0=no)"].value_counts()[1])
# patients admitted in regular ward 
print(df["Patient addmited to regular ward (1=yes, 0=no)"].value_counts()[1])
print(df[df["SARS-Cov-2 exam result"] == "positive"] ["Hemoglobin"].mean())
print(df[df["SARS-Cov-2 exam result"] == "negative"] ["Platelets"].mean())
print(df.isnull().sum().idxmax())
# Top 5 oldest patients 
oldest = df.sort_values(by= "Patient age quantile", ascending = False).head(5)
print(oldest[["Patient ID", "Patient age quantile"]])
print(df[(df["SARS-Cov-2 exam result"] == "positive") & 
         (df["Patient addmited to intensive care unit (1=yes, 0=no)"] == 1)] 
         [["SARS-Cov-2 exam result", "Patient addmited to intensive care unit (1=yes, 0=no)"]])
# percentage of covid positive 
percentage_positive = ((df["SARS-Cov-2 exam result"] == "positive").sum())/(len(df)) *100
print("The percentage of covid positive patient admitted in icu:", percentage_positive)
# Among COVID-positive patients, which is higher:
#Average Hemoglobin
#Average Platelets
Avg_hem = df[df["SARS-Cov-2 exam result"] == "positive"] ["Hemoglobin"].mean()
avg_plate = df[df["SARS-Cov-2 exam result"] == "positive"] ["Platelets"].mean()
if Avg_hem > avg_plate:
    print("Average hemoglobin has the higher value")
else:
    print("Avg_platelets has the higher value")
# new Summary table using groupby()
summary = df.groupby("SARS-Cov-2 exam result").agg(
    count = ("Patient ID", "count"),
    Avg_hemo = ("Hemoglobin","mean"),
    Avg_platelets = ("Platelets", "mean")
)
print(summary)

