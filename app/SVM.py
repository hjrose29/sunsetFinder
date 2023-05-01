import cv2
import numpy as np
import os
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from PIL import Image

# Define the path to the training data
data_path = "/Users/henry/Documents/sunsetFinder/Data/trainNew/"

# Define the classes
classes = ["Non-Sunsets", "Sunsets"]

# Initialize the lists for the features and labels
X = []
y = []

# Loop through each class
for class_index, class_name in enumerate(classes):
    # Define the path to the class folder
    class_path = os.path.join(data_path, class_name)
    # Loop through each image in the class folder
    for image_name in os.listdir(class_path):
        if(image_name == ".DS_Store"):
            continue
        
        # Load the image and convert it to grayscale
        image_path = os.path.join(class_path, image_name)
        if os.path.isfile(image_path) and os.path.getsize(image_path) > 0:
            image = Image.open(image_path)
            gray = np.array(image.convert('L'))
            # Extract the HOG features from the image
            hog = cv2.HOGDescriptor()
            features = hog.compute(gray)
            # Add the features and label to the lists
            X.append(features)
            y.append(class_index)
        else:
            print(f"Skipping empty or non-existent image: {image_path}")


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the SVM model
model = SVC(kernel='linear', C=1, gamma='scale')

# Train the model on the training set
model.fit(X_train, y_train)

# Test the model on the testing set
y_pred = model.predict(X_test)

# Print the classification report and confusion matrix
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
1