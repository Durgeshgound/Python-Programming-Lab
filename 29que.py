#Write a program using pandas to filter and group data.

import pandas as pd

# Create sample data (you can also read from CSV using pd.read_csv)
data = {
    "Name": ["Durgesh", "Rupesh", "yogesh"],
    "Department": ["IT", "HR", "IT"],
    "Salary": [50000, 40000, 60000],
    "Age": [20, 30, 28, ]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# 1. Filtering Data
# Filter employees with Salary > 45000
filtered = df[df["Salary"] > 45000]

print("\nFiltered Data (Salary > 45000):")
print(filtered)

# 2. Grouping Data
# Group by Department and calculate average salary

grouped = df.groupby("Department")["Salary"].mean()

print("\nGrouped Data (Average Salary by Department):")
print(grouped)