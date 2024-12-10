import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

file_path = "D:\Desktop\学习资料\HIstory 1354 Digital HIstoy\Sicheng-Wu-History-1354-Project\DIgital Tool Exercise\conflict_factors.csv"  
df = pd.read_csv(file_path)

print("Dataset Preview:")
print(df.head())
print("\nDataset Info:")
print(df.info())

X = df.drop(columns=['conflict']) 
y = df['conflict'] 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression(max_iter=1000)  
model.fit(X_train, y_train)  


y_pred = model.predict(X_test) 
accuracy = accuracy_score(y_test, y_pred) 
conf_matrix = confusion_matrix(y_test, y_pred) 

print(f"\nModel Accuracy: {accuracy}")
print(f"\nConfusion Matrix:\n{conf_matrix}")
