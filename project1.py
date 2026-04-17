import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# np.random.seed(42)
n = 150

a={
    "Household_ID": range(1, n+1),
    "Age_of_Household_Head": np.random.randint(25, 70, n),
    "Household_Income": np.random.randint(10000, 100000, n),
    "Education_Level": np.random.choice(["Primary", "Secondary", "Graduate", "Post-Grad"], n),
    "Family_Size": np.random.randint(1, 8, n),
    "Owns_House": np.random.choice(["Yes", "No"], n),
    "Urban_Rural": np.random.choice(["Urban", "Rural"], n)
}
df=pd.DataFrame(a)
print(df)

# # 3 #

# print(df.dtypes)

# # 4 # 

# mean_income=(df["Household_Income"].mean())
# print("mean",mean_income)

# median_income=(df["Household_Income"].median())
# print("median",median_income)

# mode_income=(df["Household_Income"].mode())
# print("mode",mode_income)

# # 5 #

# range_income = (df["Household_Income"].max() - df["Household_Income"].min())
# print("range",range_income)

# variance_income = (df["Household_Income"].var())
# print("var",variance_income)

# std_dev_income = (df["Household_Income"].std())
# print("std",std_dev_income)

# q3 = df["Household_Income"].quantile(0.75)
# q1= df["Household_Income"].quantile(0.25)
# iqr=q3-q1
# print("iqr",iqr)

# if iqr > 50000:
#     print("spred is high")
# elif iqr > 30000:
#     print("spred is mediam")
# else:
#     print("spred is low")

# # 6 #

# plt.hist(df["Household_Income"],bins=10,rwidth=0.5)
# plt.title("Income Distribution")
# plt.xlabel("Income")
# plt.ylabel("Frequency")
# plt.show()


# skew_income=df["Household_Income"].skew()
# kur_income=df["Household_Income"].kurtosis()
# print("skew",skew_income)
# print("kur",kur_income)

# 7 #

sns.kdeplot(df["Household_Income"], fill=True)
plt.title("Income Density Curve")
plt.show()

sns.boxplot(x="Education_Level", y="Family_Size", data=df)
plt.title("Family Size by Education Level")
plt.show()

sns.scatterplot(x="Age_of_Household_Head", y="Household_Income", data=df)
plt.title("Age vs Income")
plt.show()






