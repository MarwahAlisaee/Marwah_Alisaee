"""
#Generate a random dataset with two features (x1, x2) a. (10 pt) if you use a programming language . You can use a library like NumPy or Scikitlearn to generate the dataset.
import numpy as np
np.random.seed(42)
num_samples = 100
x1 = np.random.randn(num_samples)
x2 = np.random.randn(num_samples)
dataset = np.column_stack((x1, x2))
print(dataset[:5])
"""


"""
# Divide the dataset into training and test sets ,if you use a programming language . You can use a library like matplotlib

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Assuming you have a dataset called 'data' and the target variable is called 'target'

# Split the dataset into features (X) and target variable (y)
X = data.drop('target', axis=1)
y = data['target']

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Visualize the split
plt.scatter(X_train, y_train, color='blue', label='Training Set')
plt.scatter(X_test, y_test, color='red', label='Test Set')
plt.legend()
plt.show()
"""
"""
#Train the KNN classifier on the training set and determine the optimal value of k using cross-validation. You can use a library like Scikit-learn to perform cross-validation and select the optimal value of k.
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

# Load the iris dataset (or any other dataset you want to use)
iris = load_iris()
X = iris.data
y = iris.target

# Create a list of k values to try
k_values = list(range(1, 31))

# Perform cross-validation for each k value
cv_scores = []
for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X, y, cv=5)  # 5-fold cross-validation
    cv_scores.append(scores.mean())

# Find the optimal value of k with the highest cross-validation score
optimal_k = k_values[cv_scores.index(max(cv_scores))]

print("Optimal value of k:", optimal_k)

"""

# Divide the dataset into training and test sets.
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('Heart_Disease_Prediction.csv')

train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)

print('Training set shape:', train_data.shape)
print('Test set shape:', test_data.shape)
