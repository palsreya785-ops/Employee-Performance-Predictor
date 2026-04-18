import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/processed/cleaned_data.csv")

# 1. Performance Distribution
sns.countplot(x="performance", data=df)
plt.savefig("outputs/plots/performance_distribution.png")
plt.clf()

# 2. Correlation Heatmap
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.savefig("outputs/plots/correlation_heatmap.png")
plt.clf()

# 3. Scatter Plot
sns.scatterplot(x="projects_completed", y="attendance", hue="performance", data=df)
plt.savefig("outputs/plots/performance_scatter.png")
plt.clf()

# 4. Salary Distribution
sns.histplot(df["salary"], kde=True)
plt.savefig("outputs/plots/salary_distribution.png")
plt.clf()

# 5. Experience Distribution
sns.histplot(df["experience"], kde=True)
plt.savefig("outputs/plots/experience_distribution.png")
plt.clf()

# 6. Boxplot (Outliers)
sns.boxplot(data=df)
plt.savefig("outputs/plots/outliers_boxplot.png")
plt.clf()

# 7. Pairplot
sns.pairplot(df, hue="performance")
plt.savefig("outputs/plots/pairplot.png")
plt.clf()

print("EDA plots generated")
