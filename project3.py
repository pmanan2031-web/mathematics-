import numpy as np
import pandas as pd
from scipy import stats


np.random.seed(42)  # for reproducibility
n = 100  # number of records

# Generate data
df= {
 "record_id" : [f"R{i+1:03d}" for i in range(n)],
 "age" : np.random.randint(18, 75, n),
 "weight": np.random.randint(50, 100, n),

"gender" : np.random.choice(["Male", "Female", "Other"], n),

"region" : np.random.choice(["North", "South", "East", "West"], n),

"smoking_status" : np.random.choice(
    ["Smoker", "Non-Smoker", "Former Smoker"], n),

"exercise_frequency" : np.random.choice(
    ["Daily", "Weekly", "Rarely", "Never"], n),

"bmi" : np.round(np.random.uniform(18, 35, n), 1),

"blood_pressure" : np.random.randint(100, 160, n),

"diabetes" : np.random.choice([True, False], n),

"hypertension" : np.random.choice([True, False], n),

"cholesterol_level" : np.random.randint(150, 260, n),

"glucose_level" : np.random.randint(70, 180, n),

"visit_date" : pd.to_datetime(
    np.random.choice(pd.date_range("2025-01-01", "2025-12-31"), n)
)}
data=pd.DataFrame(df)
print(data)

np.random.seed(42)

# 1. Hypothesis Testing (Example)
# H0: Smoking has no effect on diabetes
# H1: Smoking affects diabetes

contingency_table = pd.crosstab(data['smoking_status'], data['diabetes'])

chi2, p, dof, expected = stats.chi2_contingency(contingency_table)

print("\nChi-square Test")
print("Chi2:", chi2)
print("p-value:", p)


# 2. Confidence Interval (Age)

mean_age = np.mean(data['age'])
std_age = np.std(data['age'], ddof=1)
n = len(data)

confidence = 0.95
z = stats.norm.ppf(1 - (1 - confidence)/2)

margin_error = z * (std_age / np.sqrt(n))

ci_lower = mean_age - margin_error
ci_upper = mean_age + margin_error

print("\nConfidence Interval (Age):")
print(ci_lower)
print(ci_upper)


# 3. One-sample t-test
# H0: mean age = 40

t_stat, p_val = stats.ttest_1samp(data['age'], 40)

print("\nOne-sample t-test:")
print("t-stat:", t_stat)
print("p-value:", p_val)


# 4. Chi-square Test (Categorical)
# Already done above



# 5. ANOVA Test (Age groups vs Weight)

group1 = data[data['age'] < 30]['weight']
group2 = data[(data['age'] >= 30) & (data['age'] < 45)]['weight']
group3 = data[data['age'] >= 45]['weight']

f_stat, p_val = stats.f_oneway(group1, group2, group3)

print("\nANOVA Test:")
print("F-stat:", f_stat)
print("p-value:", p_val)


# 6. Covariance & Correlation

cov_matrix = np.cov(data['age'], data['weight'])
correlation = np.corrcoef(data['age'], data['weight'])

print("\nCovariance Matrix:")
print(cov_matrix)

print("\nCorrelation Matrix:")
print(correlation)


# 7. Final Interpretation

alpha = 0.05

print("\n--- Interpretation ---")

if p < alpha:
    print("Chi-square: Reject H0 (Smoking affects diabetes)")
else:
    print("Chi-square: Fail to Reject H0")

if p_val < alpha:
    print("ANOVA: Reject H0 (Groups differ)")
else:
    print("ANOVA: Fail to Reject H0")