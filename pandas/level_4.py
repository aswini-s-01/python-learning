import pandas as pd 
df = pd.read_excel("Covid dataset.xlsx")
# filtering
positive = df[df["SARS-Cov-2 exam result"] == "positive"]
print(positive)
# negative results 
negative = df[df["SARS-Cov-2 exam result"] == "negative"]
print(negative)
# patients admitted to icu
icu_patient = df[df["Patient addmited to intensive care unit (1=yes, 0=no)"]== 1]
print(icu_patient)
# patient admitted to icu and covid positive 
covid_postive = df[
        (df["Patient addmited to intensive care unit (1=yes, 0=no)"] == 1) &
        (df["SARS-Cov-2 exam result"] == "positive")]
print(covid_postive)
print(df[df['Patient age quantile'] > 15])
# patient age is greater than 15 and has covid positive 
age_covid_positive = df[(df["Patient age quantile"] > 15) & (df["SARS-Cov-2 exam result"] == "positive")] 
print(age_covid_positive)