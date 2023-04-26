from sklearn import svm
from sklearn.metrics import accuracy_score
import numpy as np

# Load the preprocessed data from the .npz files
X_train = np.load('X_train.npz')['X_train']
X_test = np.load('X_test.npz')['X_test']
y_train = np.load('y_train.npz')['y_train']
y_test = np.load('y_test.npz')['y_test']

print("Data loaded from .npz files.")

# Train an SVM classifier
clf = svm.SVC(kernel='linear', C=1)
clf.fit(X_train, y_train)

print("SVM model trained.")

# Make predictions on the testing set
y_pred = clf.predict(X_test)

print("Predictions made on the testing set.")

# Calculate the accuracy of the classifier
accuracy_Dec = accuracy_score(y_test, y_pred)
accuracy = accuracy_Dec * 100
print("Accuracy:", accuracy)
