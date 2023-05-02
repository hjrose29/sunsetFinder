from ast import increment_lineno
from cgi import test
import time
import numpy as np
import keras
from keras import backend as K
from keras.models import Sequential
from keras.layers import Activation, Dropout
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
from PIL import Image

from hue import get_dominant_hue



train_path =  "/Users/henry/Documents/sunsetFinder/Data/trainNew"
test_path = "/Users/henry/Documents/sunsetFinder/Data/test" 
validation_path = "/Users/henry/Documents/sunsetFinder/Data/valid"

train_batches = ImageDataGenerator().flow_from_directory(train_path, target_size=(300,300), classes=['Sunsets','Non-Sunsets'], batch_size=10)
test_batches = ImageDataGenerator().flow_from_directory(test_path, target_size=(300,300), classes=None, class_mode=None, batch_size=10)
valid_batches = ImageDataGenerator().flow_from_directory(validation_path, target_size=(300,300), classes=['Sunsets','Non-Sunsets'], batch_size=4)

model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(300,300,3)),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(pool_size=(2,2)),
    Conv2D(128, (3,3), activation='relu'),
    Conv2D(256, (3,3), activation='relu'),
    MaxPooling2D(pool_size=(2,2)),
    Conv2D(512, (3,3), activation='relu'),
    Flatten(),
    Dense(2,activation='softmax'),
    ]
)
model.compile(Adam(lr=.001), loss='categorical_crossentropy',metrics=['accuracy'])


history = model.fit_generator(train_batches, steps_per_epoch=len(train_batches), 
                    validation_data=valid_batches, validation_steps=len(valid_batches),
                    epochs=1, verbose=2)
###3 Epochs seems to work decently. 66% success rate
###Make Predictions
import cv2
from keras.preprocessing import image
from keras.utils import img_to_array

def extract_dominant_hue(filepath):
    img = cv2.imread(filepath)
    return get_dominant_hue(img)

def classify_image(filepath):
    img = Image.open(filepath)
    img = img.resize((244, 244))
    img = np.array(img)
    hue = extract_dominant_hue(filepath) # Extract dominant hue
    img = np.concatenate([img, hue], axis=-1) # Concatenate image and hue
    img /= 255.
    fp = io.BytesIO()
    np.save(fp, img)
    fp.seek(0)
    prediction = history.model.predict(np.load(fp))[0]
    if prediction[0] > prediction[1]:
        return 1 # Image is a sunset
    else:
        return 0 # Image is not a sunset




s = "/Sunsets/"
n = "/Non-Sunsets/"


totCount1 = 0
count1 = 0
for i in os.listdir(train_path + s):
    totCount1 += 1
    if(i == ".DS_Store"):
        continue
    if(classify_image(train_path + s + i) == 1):
        print(".")
        count1 += 1


totCount2 = 0
count2 = 0
for i in os.listdir(train_path + n):
    totCount2 += 1
    if(i == ".DS_Store"):
        continue
    if(classify_image(train_path + n + i) == 1):
        count2 += 1


print("Identified Sunset as Sunset: " + str(count1/totCount1))
print("Identified Non-Sunset as Sunset: " + str(count2/totCount2))




###################################
####This code generates a threshold
###################################




# path = "/Users/henry/Documents/sunsetFinder/toSplit/"
# newPath = "/Users/henry/Documents/sunsetFinder/algoSays/"
# newnewPath = "/Users/henry/Documents/sunsetFinder/algoSays/better/"

# total = 0
# count = 0 
# for i in os.listdir(newPath):
#     if(i == ".DS_Store"):
#         continue

#     total += classify_image(newPath + i)[0]
#     count += 1

# avg = total/count

# print(total)
# print(count)
# print("Second Pass")

# count = 0
# totCount = 0
# for i in os.listdir(newPath):
#     if(i == ".DS_Store"):
#         continue
#     totCount += 1

#     if(classify_image(newPath + i)[0] < avg):
#         shutil.copyfile(newPath + i, newnewPath + i)
#         count += 1
#         print("HIT")


# print(count)
# print(totCount)


