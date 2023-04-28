from ast import increment_lineno
from cgi import test
import time
import numpy as np
import keras
from keras import backend as K
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense, Flatten
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
from keras.layers.normalization import batch_normalization
from keras.layers.convolutional import *
import os
from sklearn.metrics import confusion_matrix
import itertools
import shutil

train_path =  "/Users/henry/Documents/sunsetFinder/Data/trainNew"
test_path = "/Users/henry/Documents/sunsetFinder/Data/test" 
validation_path = "/Users/henry/Documents/sunsetFinder/Data/valid"

train_batches = ImageDataGenerator().flow_from_directory(train_path, target_size=(244,244), classes=['Sunsets','Non-Sunsets'], batch_size=10)
test_batches = ImageDataGenerator().flow_from_directory(test_path, target_size=(244,244), classes=None, class_mode=None, batch_size=10)
valid_batches = ImageDataGenerator().flow_from_directory(validation_path, target_size=(244,244), classes=['Sunsets','Non-Sunsets'], batch_size=4)

model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(244,244,3)),
    Flatten(),
    Dense(2,activation='softmax'),
    ]
)

model.compile(Adam(lr=.0001), loss='categorical_crossentropy',metrics=['accuracy'])

model.fit_generator(train_batches, steps_per_epoch=4, validation_data=valid_batches,validation_steps=4, epochs=5,verbose=2)


###Make Predictions
import cv2
from keras.preprocessing import image
from keras.utils import img_to_array


def classify_image(filepath):
    img = cv2.imread(filepath)
    img = cv2.resize(img, (244,244))
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img /= 255.
    prediction = model.predict(img)[0]
    return prediction
    # if prediction[0] > prediction[1]:
    #     return 1 # Image is a sunset
    # else:
    #     return 0 # Image is not a sunset

###################################
####This code generates a threshold
###################################


path = "/Users/henry/Documents/sunsetFinder/toSplit/"
newPath = "/Users/henry/Documents/sunsetFinder/algoSays/"

total = 0
count = 0 
for i in os.listdir(path):
    if(i == ".DS_Store"):
        continue

    total += classify_image(path + i)[0]
    count += 1

avg = total/count

print(total)
print(count)
print("Second Pass")

for i in os.listdir(path):
    if(i == ".DS_Store"):
        continue

    if(classify_image(path + i)[0] < avg / 5):
        shutil.copyfile(path + i, newPath + i)
        print("HIT")

