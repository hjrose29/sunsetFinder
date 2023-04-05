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


# Function to Extract features from the images
def image_feature(direc):
    model = InceptionV3(weights='imagenet', include_top=False)
    features = []
    img_name = []
    for i in tqdm(direc):
        fname = 'TestPictures' + '/' + i
        img = image.load_img(fname, target_size=(224, 224))
        x = img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        feat = model.predict(x)
        feat = feat.flatten()
        features.append(feat)
        img_name.append(i)
    return features, img_name


img_path = os.listdir('TestPictures')
img_features, img_name = image_feature(img_path)


# Creating Clusters
k = 2
clusters = KMeans(k, random_state=40, n_init=10)
clusters.fit(img_features)

image_cluster = pd.DataFrame(img_name, columns=['image'])
image_cluster["clusterid"] = clusters.labels_

# Made folder to separate images
os.mkdir('sunset')
os.mkdir('not_sunset')
for i in range(len(image_cluster)):
    if image_cluster['clusterid'][i] == 0:
        shutil.move(os.path.join('TestPictures', image_cluster['image'][i]), 'sunset')
    else:
        shutil.move(os.path.join('TestPictures', image_cluster['image'][i]), 'not_sunset')
