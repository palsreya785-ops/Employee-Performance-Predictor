import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report

df = pd.read_csv("data/processed/cleaned_data.csv")

X = df.drop("performance", axis=1)
y = df["performance"]

model = joblib.load("models/employee_model.pkl")

y_pred = model.predict(X)

# Confusion Matrix
cm = confusion_matrix(y, y_pred)
sns.heatmap(cm, annot=True)
plt.savefig("outputs/plots/confusion_matrix.png")
plt.clf()

# Feature Importance
importances = model.feature_importances_
plt.barh(X.columns, importances)
plt.savefig("outputs/plots/feature_importance.png")
plt.clf()

# Save report
report = classification_report(y, y_pred)
with open("outputs/reports/metrics.txt", "w") as f:
    f.write(report)

print(report)
