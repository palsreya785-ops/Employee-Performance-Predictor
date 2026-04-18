Employee Performance Predictor using Data Analytics

📌 Project Overview

This project predicts employee performance (High / Medium / Low) using Machine Learning based on factors like experience, salary, training hours, attendance, and project completion.

It simulates a real-world HR analytics system used by companies to support decision-making in performance evaluation.

---

🎯 Problem Statement

Organizations need to:

- Identify high-performing employees
- Detect low performers early
- Improve training strategies
- Support promotion and retention decisions

This project builds a data-driven system to solve this.

---

💼 Business Value

- Helps HR make data-driven decisions
- Improves employee productivity
- Reduces bias in performance evaluation
- Enables targeted training programs

---

🧠 Machine Learning Approach

- Type: Classification (High / Medium / Low)
- Model Used: Random Forest Classifier

Features Used:

- Age
- Experience
- Salary
- Training Hours
- Projects Completed
- Attendance

---

⚙️ Project Architecture

Data Generation → Preprocessing → EDA → Model Training → Evaluation → Prediction

---

📁 Folder Structure

Employee-Performance-Predictor/
│
├── data/
├── src/
├── models/
├── outputs/
├── images/
├── main.py
├── requirements.txt
└── README.md

---

📊 Visualizations

📌 Performance Distribution

"Performance Distribution" (images/performance_distribution.png)

📌 Correlation Heatmap

"Correlation Heatmap" (images/correlation_heatmap.png)

📌 Performance Scatter Plot

"Scatter Plot" (images/performance_scatter.png)

📌 Feature Importance

"Feature Importance" (images/feature_importance.png)

📌 Confusion Matrix

"Confusion Matrix" (images/confusion_matrix.png)

---

📈 Model Evaluation

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1-score

Full evaluation report available in:
outputs/reports/metrics.txt

---

🔮 Prediction Example

Input:
Age: 30
Experience: 5
Projects: 8
Attendance: 0.85

Output:
Predicted Performance: Medium

---

▶️ How to Run the Project

Step 1: Clone Repository

git clone https://github.com/palsreya785-ops/Employee-Performance-Predictor.git
cd Employee-Performance-Predictor

---

Step 2: Create Virtual Environment

python -m venv venv
venv\Scripts\activate

---

Step 3: Install Dependencies

pip install -r requirements.txt

---

Step 4: Run Project

python main.py

---

🧪 Outputs Generated

- Dataset (CSV)
- Cleaned data
- Trained model (.pkl)
- Graphs (.png)
- Evaluation report



🧑‍💻 Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Joblib

---

🚀 Future Improvements

- Use real HR dataset
- Add Streamlit dashboard
- Apply deep learning models
- Add employee attrition prediction
- Deploy as web application

---

💡 Key Learnings

- End-to-end ML pipeline development
- Data preprocessing and visualization
- Model training and evaluation
- Real-world project structuring

---

🏁 Conclusion

This project demonstrates how machine learning can be applied to HR analytics for improving employee performance and business decision-making.

---

⭐ If you like this project, give it a star!
