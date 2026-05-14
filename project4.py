import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import lognorm
from scipy.stats import powerlaw
from scipy.stats import probplot
from scipy.stats import boxcox
from scipy.stats import zscore
from scipy.stats import norm


np.random.seed(42)

n=100

tra_id=np.arange(1000,1000+n)
print(tra_id)

cus_id=np.random.randint(1,100,n)
print(cus_id)

tra_amo=np.random.randint(10000,50000,n)
print(tra_amo)

tra_date = np.random.choice(
    pd.date_range("2025-01-01", periods=120),
    n)
print(tra_date)

tra_count=np.random.randint(1,15,n)
print(tra_count)

region=np.random.choice(["north","south","east","west"],n)
print(region)

status=np.random.choice(["success","fail"],n)
print(status)

# 1 #

# "Bernoulli Data"
Bernoulli_Data = np.where(
    status == "success",
    1,
    0
    
)
print(Bernoulli_Data)

# Probability of success
p = np.mean(Bernoulli_Data)

print("\nProbability of Success :", p)

# 2 #

from scipy.stats import poisson

lam=np.mean(tra_count)
x = np.arange(1,15)

pmf=poisson.pmf(x,lam)
print("1 to 14",pmf)

# 3 #


shape, loc, scale = lognorm.fit(tra_amo)

x = np.linspace(
    tra_amo.min(),
    tra_amo.max(),
    200
)

pdf_lognorm = lognorm.pdf(
    x,
    shape,
    loc,
    scale
)

plt.figure(figsize=(7,4))

sns.histplot(
    ["tra_amo"],
    bins=30,
    stat="density"
)

plt.plot(x, pdf_lognorm)

plt.title("Log-Normal Distribution Fit")
plt.show()


#  Power Law Distribution


a, loc, scale = powerlaw.fit([tra_amo])

pdf_powerlaw = powerlaw.pdf(
    x,
    a,
    loc,
    scale
)

plt.figure(figsize=(7,4))

sns.histplot(
    ["tra_amo"],
    bins=30,
    stat="density"
)

plt.plot(x, pdf_powerlaw)

plt.title("Power Law Distribution Fit")
plt.show()


# 4. Q-Q Plot


plt.figure(figsize=(6,6))

probplot(
    ["tra_amo"],
    dist="norm",
    plot=plt
)

plt.title("Q-Q Plot")
plt.show()


# 5. Box-Cox Transformation


boxcox_data, lambda_value = boxcox(tra_amo)

print("\nBox-Cox Lambda:", lambda_value)

plt.figure(figsize=(7,4))

sns.histplot(boxcox_data, bins=30)

plt.title("Box-Cox Transformed Data")
plt.show()


# 6. Z-score and Probability > 5000


Z_score = zscore([tra_amo])

print("\nZ-Scores:")

mean = tra_amo.mean()
std = tra_amo.std()

# Probability amount > 5000

prob = 1 - norm.cdf(
    5000,
    mean,
    std
)

print("\nProbability(Transaction > 5000):", prob)

# 7. PDF and CDF


x = np.linspace(
    tra_amo.min(),
    tra_amo.max(),
    200
)

pdf = norm.pdf(x, mean, std)
cdf = norm.cdf(x, mean, std)

# PDF Plot

plt.figure(figsize=(7,4))
plt.plot(x, pdf)
plt.title("PDF of Transaction Amount")
plt.xlabel("Amount")
plt.ylabel("Density")
plt.show()

# CDF Plot

plt.figure(figsize=(7,4))
plt.plot(x, cdf)
plt.title("CDF of Transaction Amount")
plt.xlabel("Amount")
plt.ylabel("Probability")
plt.show()
