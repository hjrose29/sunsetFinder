from keras.applications.inception_v3 import InceptionV3
from keras.applications.inception_v3 import preprocess_input
import keras.utils as image
from keras.utils import img_to_array
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from tqdm import tqdm
import os
import shutil


# function to extract features from the images
def image_feature(directory):
    model = InceptionV3(weights='imagenet', include_top=False)
    features = []
    img_name = []
    # loop over images and extract their features
    for i in tqdm(directory):
        file_name = 'TestPictures' + '/' + i
        picture = image.load_img(file_name, target_size=(256, 256))  # resizes image to 256x256
        x = img_to_array(picture)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        feat = model.predict(x)  # extract features
        feat = feat.flatten()
        features.append(feat)   # adds the features to a list
        img_name.append(i)  # appends the file name to its features
    return features, img_name


folder_path = os.listdir('TestPictures')
image_features, image_name = image_feature(folder_path)


# cluster the images with kmeans
k = 2   # number of clusters
clusters = KMeans(k, random_state=40, n_init=10)
clusters.fit(image_features)

# data frame for file names with their cluster ids
image_cluster = pd.DataFrame(image_name, columns=['image'])
image_cluster["cluster_id"] = clusters.labels_

# check if the directories exist
if not os.path.exists('sunset'):
    os.mkdir('sunset')
if not os.path.exists('not_sunset'):
    os.mkdir('not_sunset')
# add picture to respective directory based on their cluster id
for j in range(len(image_cluster)):
    if image_cluster['cluster_id'][j] == 0:
        shutil.move(os.path.join('TestPictures', image_cluster['image'][j]), 'not_sunset')
    else:
        shutil.move(os.path.join('TestPictures', image_cluster['image'][j]), 'sunset')
