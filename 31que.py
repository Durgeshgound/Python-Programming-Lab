#Write a program combining numpy, pandas, and matplotlib for simple data analysis.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Create Data using NumPy
np.random.seed(0)
data = {
    "Day": np.arange(1, 11),
    "Sales": np.random.randint(100, 500, 10),
    "Profit": np.random.randint(20, 100, 10)
}

# 2. Create DataFrame using pandas
df = pd.DataFrame(data)

print("Dataset:")
print(df)

# 3. Basic Analysis
print("\nTotal Sales:", np.sum(df["Sales"]))
print("Average Profit:", np.mean(df["Profit"]))
print("Maximum Sales:", np.max(df["Sales"]))

# 4. Plot using Matplotlib

# Line graph for Sales
plt.figure()
plt.plot(df["Day"], df["Sales"])
plt.title("Sales Over Days")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.show()

# Bar graph for Profit
plt.figure()
plt.bar(df["Day"], df["Profit"])
plt.title("Profit by Day")
plt.xlabel("Day")
plt.ylabel("Profit")
plt.show()