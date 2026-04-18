import pandas as pd

df = pd.read_csv("data/raw/employee_data.csv")

# Introduce missing values (for demo)
df.loc[df.sample(frac=0.1).index, "salary"] = None

# Fill missing values
df.fillna(df.median(numeric_only=True), inplace=True)

df.to_csv("data/processed/cleaned_data.csv", index=False)

print("Data cleaned")
