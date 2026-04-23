import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Q1: Create Dataset
np.random.seed(42)
n = 200

data = pd.DataFrame({
    "study_hours": np.random.randint(5, 20, n),
    "attendance": np.random.randint(50, 100, n),
    "group_discussion": np.random.choice(["Yes", "No"], n),
    "previous_test_score": np.random.randint(30, 100, n)
})

# Pass/Fail Logic
data["final_exam_pass"] = np.where(
    (data["study_hours"] > 10) &
    (data["attendance"] > 75) &
    (data["previous_test_score"] > 50),
    "Pass", "Fail"
)

print(" Dataset Preview")
print(data.head())


# Q2: Basic Probability
total = len(data)
pass_students = len(data[data["final_exam_pass"] == "Pass"])

P_pass = pass_students / total

print(" Probability of Passing =", round(P_pass, 3))


# Q3: Three Probability Events
study_event = len(data[data["study_hours"] > 10]) / total
attendance_event = len(data[data["attendance"] > 80]) / total
pass_event = pass_students / total

print("Q3: Probability Events")
print("P(Study > 10 hrs) =", round(study_event, 3))
print("P(Attendance > 80%) =", round(attendance_event, 3))
print("P(Pass) =", round(pass_event, 3))


# Q4: Mean and Variance (Binomial)
n_trials = 3
p = P_pass

mean = n_trials * p
variance = n_trials * p * (1 - p)

print("Mean =", round(mean, 3))
print("Variance =", round(variance, 3))


# Q5: Contingency Table
table = pd.crosstab(data["group_discussion"], data["final_exam_pass"])

print("Contingency Table")
print(table)

joint = table.loc["Yes", "Pass"] / total
conditional = table.loc["Yes", "Pass"] / table.loc["Yes"].sum()

print("Joint Probability =", round(joint, 3))
print("Conditional Probability =", round(conditional, 3))


# Q6: Bayes Theorem
high_attendance = data[data["attendance"] > 80]

P_high = len(high_attendance) / total
P_pass = pass_students / total

P_high_given_pass = len(
    data[(data["final_exam_pass"] == "Pass") & (data["attendance"] > 80)]
) / pass_students

bayes = (P_high_given_pass * P_pass) / P_high

print("P(Pass | High Attendance) =", round(bayes, 3))


# Q7: Graphs

# Bar Chart
data["final_exam_pass"].value_counts().plot(kind="bar")
plt.title("Pass vs Fail")
plt.show()

# Scatter Plot
plt.scatter(data["study_hours"], data["previous_test_score"])
plt.title("Study Hours vs Test Score")
plt.xlabel("Study Hours")
plt.ylabel("Test Score")
plt.show()


# Q8: Final Conclusion
print("Q8: Conclusion")
print("Students who study more, attend regularly, and participate in discussions are more likely to pass.")








