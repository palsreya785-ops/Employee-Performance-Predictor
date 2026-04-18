import os

print("Step 1")
os.system("python src/data_generator.py")

print("Step 2")
os.system("python src/preprocessing.py")

print("Step 3")
os.system("python src/eda.py")

print("Step 4")
os.system("python src/model.py")

print("Step 5")
os.system("python src/evaluate.py")

print("Step 6")
os.system("python src/predict.py")

print("All steps completed!")
