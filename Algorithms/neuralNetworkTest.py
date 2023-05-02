# import tflearn
# from tflearn.layers.conv import conv_2d, max_pool_2d
# from tflearn.layers.core import input_data, dropout, fully_connected
# from tflearn.layers.estimator import regression
# import tflearn.datasets.mnist as mnist


# # # plot dog photos from the dogs vs cats dataset
# # from matplotlib import pyplot
# # from matplotlib.image import imread
# # # define location of dataset
# # folder = 'Data/'
# # sunsetPath = folder + "Sunsets/"
# # # plot first few images
# # count = 0

# # for i in os.listdir(sunsetPath):
# #     print(i)
# # for i in os.listdir(folder + "Sunsets"):
# #         if(i != ".DS_Store"):
# #                 count += 1
# #                 # define subplot
# #                 pyplot.subplot(10,10, count)
# #                 # define filename
# #                 filename = sunsetPath + i
# #                 # load image pixels
# #                 image = imread(filename)
# #                 # plot raw pixel data
# #                 pyplot.imshow(image)
# # show the figure
# # pyplot.show()


# # seed(1)
# # val_ratio = 0.25
# # #Split data 75-25, run for Sunsets and Non-Sunsets
# # src_directory = 'toSplit/Sunsets'
# # for file in listdir(src_directory):
# #         src = src_directory + '/' + file
# #         dst_dir = 'Data/train/Sunsets'
# #         if random() < val_ratio:dst_dir = 'Data/test/Sunsets'
# #         dst = dst_dir + "/" + file
# #         copyfile(src, dst)


# #Develop baseline cnn

# # baseline model for the dogs vs cats dataset


# import numpy as np
# import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras import layers
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# train_generator = train_datagen.flow_from_directory(
#     r'/Users/henry/Documents/sunsetFinder/Data/train',
#     target_size=(300, 300),
#     batch_size=128,
#     class_mode='binary'
# )

# model = tf.keras.models.Sequential([
#     #Note the input shape is the size of the image 300x300 with 3 bytes color
    
#     tf.keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=(300, 300, 3)),
#     tf.keras.layers.MaxPooling2D(2, 2),
    
#     tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
#     tf.keras.layers.MaxPooling2D(2,2),
       
#     tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
#     tf.keras.layers.MaxPooling2D(2,2),
    
#     tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
#     tf.keras.layers.MaxPooling2D(2,2),
    
#     tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
#     tf.keras.layers.MaxPooling2D(2,2),
    
#     # Flatten the results to feed into a DNN
#     tf.keras.layers.Flatten(),
    
#     tf.keras.layers.Dense(512, activation='relu'),
#     tf.keras.layers.Dense(512, activation='relu'),
    
#     tf.keras.layers.Dense(1, activation='sigmoid')
# ])

# from tensorflow.keras.optimizers import RMSprop

# model.compile(loss="binary_crossentropy",
#              optimizer=RMSprop(learning_rate=0.0001),
#              metrics=['accuracy'])


# history = model.fit(
#     train_generator,
#     steps_per_epoch=8,
#     epochs=15,
#     verbose=1,
#     validation_data = validation_generator,
#     validation_steps = 8
# )


# import matplotlib.pyplot as plt
# plt.plot(history.history['accuracy'])
# plt.plot(history.history['val_accuracy'])
# plt.title('Model Accuracies')
# plt.ylabel('Accuracy')
# plt.xlabel('Epoch')
# plt.legend(['train', 'test'], loc='best')
# plt.show()
import os
import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
import tflearn.datasets.mnist as mnist
from PIL import Image
import base64

with open("/Users/henry/Documents/sunsetFinder/Data/test/Sunsets" + "/" + "20210206-1720.jpg", "rb") as image2string:
        testImage = base64.b64encode(image2string.read())


X = []
Y = []

for i in os.listdir("/Users/henry/Documents/sunsetFinder/Data/train/Non-Sunsets"):
    if(i == ".DS_Store"):
        continue

    
    with open("/Users/henry/Documents/sunsetFinder/Data/train/Non-Sunsets" + "/" + i, "rb") as image2string:
        converted_string = base64.b64encode(image2string.read())
    X.append(converted_string)
    Y.append("Non-Sunset")

for i in os.listdir("/Users/henry/Documents/sunsetFinder/Data/train/Sunsets"):
    if(i == ".DS_Store"):
        continue

    with open("/Users/henry/Documents/sunsetFinder/Data/train/Sunsets" + "/" + i, "rb") as image2string:
        converted_string = base64.b64encode(image2string.read())
    X.append(converted_string)
    Y.append("Sunset")


test_x = []
test_y = []
for i in os.listdir("/Users/henry/Documents/sunsetFinder/Data/test/Non-Sunsets"):
    if(i == ".DS_Store"):
        continue

    with open("/Users/henry/Documents/sunsetFinder/Data/test/Non-Sunsets" + "/" + i, "rb") as image2string:
        converted_string = base64.b64encode(image2string.read())
    X.append(converted_string)
    Y.append("Non-Sunset")

for i in os.listdir("/Users/henry/Documents/sunsetFinder/Data/test/Sunsets"):
    if(i == ".DS_Store"):
        continue
    
    with open("/Users/henry/Documents/sunsetFinder/Data/test/Sunsets" + "/" + i, "rb") as image2string:
        converted_string = base64.b64encode(image2string.read())
    X.append(converted_string)
    Y.append("Sunset")


convnet = input_data(shape=[None, 28, 28, 1], name='input')

convnet = conv_2d(convnet, 32, 2, activation='relu')
convnet = max_pool_2d(convnet, 2)

convnet = conv_2d(convnet, 64, 2, activation='relu')
convnet = max_pool_2d(convnet, 2)

convnet = fully_connected(convnet, 1024, activation='relu')
convnet = dropout(convnet, 0.8)

convnet = fully_connected(convnet, 10, activation='softmax')
convnet = regression(convnet, optimizer='adam', learning_rate=0.01, loss='categorical_crossentropy', name='targets')

model = tflearn.DNN(convnet)
model.fit({'input': X}, {'targets': Y}, n_epoch=10, validation_set=({'input': test_x}, {'targets': test_y}),
          snapshot_step=500, show_metric=True, run_id='mnist')



import numpy as np
print("-------------------------")
print(np.round(model.predict("/Users/henry/Documents/sunsetFinder/Data/test/Sunsets" + "/" + "20210206-1720.jpg")))