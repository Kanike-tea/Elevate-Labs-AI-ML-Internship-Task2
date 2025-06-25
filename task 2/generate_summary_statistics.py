import pandas as pd
df = pd.read_csv('Titanic-Dataset.csv')

# Summary statistics for numerical columns
print(df.describe())

# Select only numeric columns
numeric_df = df.select_dtypes(include='number')

# Mean
print("\nMean:\n", numeric_df.mean(numeric_only=True), "\n")

# Median
print("Median:\n", numeric_df.median(numeric_only=True), "\n")

# Mode (may have multiple values per column)
print("Mode:\n", numeric_df.mode(numeric_only=True).iloc[0], "\n")

# Standard Deviation
print("Standard Deviation:\n", numeric_df.std(numeric_only=True), "\n")
