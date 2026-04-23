# Student Final Exam Probability Analysis

## Project Overview
This project analyzes student performance data using **Python, Pandas, NumPy, and Matplotlib**.

The main goal is to study how different factors such as:

- Study hours
- Attendance percentage
- Group discussion participation
- Previous test score

affect the probability of passing the final exam.

The project also covers important **probability and statistics concepts** like:

- Basic probability
- Conditional probability
- Joint probability
- Bayes’ theorem
- Mean and variance of binomial distribution
- Data visualization

---

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib

---

## Dataset Information
The dataset is **synthetically generated** using NumPy.

Total records: **200 students**

### Columns
| Column Name | Description |
|------------|-------------|
| study_hours | Number of study hours |
| attendance | Attendance percentage |
| group_discussion | Participation in discussion (Yes/No) |
| previous_test_score | Previous exam score |
| final_exam_pass | Pass/Fail result |

---

## Pass/Fail Logic
A student is marked as **Pass** if:

- Study hours > 10
- Attendance > 75
- Previous test score > 50

Otherwise, the student is marked as **Fail**.

```python
(data["study_hours"] > 10) &
(data["attendance"] > 75) &
(data["previous_test_score"] > 50)
