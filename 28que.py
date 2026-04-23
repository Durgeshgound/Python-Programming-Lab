#Write a program using pandas to read a CSV file and perform basic analysis.

import pandas as pd

# Read CSV file
df = pd.read_csv("data.csv")

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Display basic information about dataset
print("\nDataset Info:")
print(df.info())

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Display column names
print("\nColumn Names:")
print(df.columns)

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())