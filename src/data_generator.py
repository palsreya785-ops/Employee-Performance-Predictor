import pandas as pd
import numpy as np

np.random.seed(42)
n = 500

df = pd.DataFrame({
    "age": np.random.randint(22, 60, n),
    "experience": np.random.randint(0, 20, n),
    "salary": np.random.randint(20000, 150000, n),
    "training_hours": np.random.randint(0, 100, n),
    "projects_completed": np.random.randint(1, 20, n),
    "attendance": np.random.uniform(0.5, 1.0, n)
})
# Create performance labels
conditions = [
    (df["projects_completed"] > 10) & (df["attendance"] > 0.8),
    (df["projects_completed"] > 5)
]

choices = ["High", "Medium"]
df["performance"] = np.select(conditions, choices, default="Low")

df.to_csv("data/raw/employee_data.csv", index=False)
print("Dataset created")
print("✅ Dataset created successfully!")