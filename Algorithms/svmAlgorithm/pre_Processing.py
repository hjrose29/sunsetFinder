import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the dataset from the .npz file
dataset_file = 'Sunset_dataset.npz'
with np.load(dataset_file, allow_pickle=True) as npz:
    data = npz['data'].tolist()

# Extract the features and labels from the dictionary
X = []
y = []
for key in data.keys():
    X.append(data[key]['features'])
    y.append(data[key]['label'])

# Convert the lists to numpy arrays
X = np.array(X)
y = np.array(y)

print("Dataset shape:", X.shape)

# Preprocess the features using StandardScaler
scaler = StandardScaler()
X = scaler.fit_transform(X)

print("Data preprocessing completed.")

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training and testing data split completed.")
print("Training data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

# Save the preprocessed data to .npz files
np.savez('X_train.npz', X_train=X_train)
np.savez('X_test.npz', X_test=X_test)
np.savez('y_train.npz', y_train=y_train)
np.savez('y_test.npz', y_test=y_test)

print("Data saved to .npz files.")
