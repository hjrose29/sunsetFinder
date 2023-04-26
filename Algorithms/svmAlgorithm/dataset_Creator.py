import cv2
import os
import numpy as np
import shutil

# Path to the folder containing the images
image_folder = '/Users/mxrksworld/Downloads/svmAlgorithm/Sunsets'
# Path to the folder to move processed images
processed_folder = '/Users/mxrksworld/Downloads/svmAlgorithm/processed_images'

# Path to the dataset file
dataset_file = '/Users/mxrksworld/Downloads/svmAlgorithm/Sunset_dataset.npz'

# Check if the processed folder exists, create it if not
if not os.path.exists(processed_folder):
    os.makedirs(processed_folder)

# Initialize dictionary to store features and labels
data = {}

# Check if the dataset file exists, load data from it if it does
if os.path.exists(dataset_file):
    with np.load(dataset_file, allow_pickle=True) as npz:
        data = npz['data'].tolist()


# Set a fixed length for the feature vectors
feature_length = 10000

# Loop through all images in the folder
for count, filename in enumerate(os.listdir(image_folder)):
    if count >= 100:
        break
    if filename.endswith('.jpg'): # Change the file extension if necessary
        print(f'Processing {filename}...')
        # Read the image using OpenCV
        image = cv2.imread(os.path.join(image_folder, filename))

        # Extract HOG features using OpenCV
        hog = cv2.HOGDescriptor()
        features = hog.compute(image)

        # Pad or truncate the feature vector to the fixed length
        if features.shape[0] < feature_length:
            features = np.concatenate((features, np.zeros((feature_length - features.shape[0], 1))))
        elif features.shape[0] > feature_length:
            features = features[:feature_length]

        # Assign labels based on the filename prefixes
        if filename.startswith('good_'):
            label = 1
        elif filename.startswith('bad_'):
            label = 0
        else:
            label = None

        # Add features and label to the dictionary
        if label is not None:
            data[filename] = {'filename': filename, 'label': label, 'features': features}

        # Move the processed image to the processed folder
        shutil.move(os.path.join(image_folder, filename), os.path.join(processed_folder, filename))

        # If we have processed 10 images, save the data to the dataset file
        if count % 10 == 0 and count != 0:
            print('Updating dataset...')
            filenames = [d for d in data.keys()]
            np.savez_compressed(dataset_file, data=data, filenames=filenames)

# Save the data to the dataset file after all the images have been processed
if len(data) > 0:
    print('Updating dataset...')
    filenames = [d for d in data.keys()]
    np.savez_compressed(dataset_file, data=data, filenames=filenames)

print('Done processing images.')
