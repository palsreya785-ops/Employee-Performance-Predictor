import joblib
import pandas as pd

model = joblib.load("models/employee_model.pkl")

sample = pd.DataFrame({
    "age": [30],
    "experience": [5],
    "salary": [50000],
    "training_hours": [40],
    "projects_completed": [8],
    "attendance": [0.85]
})

prediction = model.predict(sample)
print("Predicted Performance:", prediction[0])
