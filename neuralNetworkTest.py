from os import makedirs
from os import listdir
from shutil import copyfile
from random import seed
from random import random
from numpy import asarray
from numpy import save
import sys
from matplotlib import pyplot
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.optimizers import SGD
from keras.preprocessing.image import ImageDataGenerator


# plot dog photos from the dogs vs cats dataset
from matplotlib import pyplot
from matplotlib.image import imread
# define location of dataset
folder = 'Data/'
sunsetPath = folder + "Sunsets/"
# plot first few images
count = 0

# for i in os.listdir(sunsetPath):
#     print(i)
# for i in os.listdir(folder + "Sunsets"):
#         if(i != ".DS_Store"):
#                 count += 1
#                 # define subplot
#                 pyplot.subplot(10,10, count)
#                 # define filename
#                 filename = sunsetPath + i
#                 # load image pixels
#                 image = imread(filename)
#                 # plot raw pixel data
#                 pyplot.imshow(image)
# show the figure
# pyplot.show()


seed(1)
val_ratio = 0.25
#Split data 75-25, run for Sunsets and Non-Sunsets
src_directory = 'toSplit/Non-Sunsets'
for file in listdir(src_directory):
        src = src_directory + '/' + file
        dst_dir = 'Data/train/Non-Sunsets'
        if random() < val_ratio:dst_dir = 'Data/test/Non-Sunsets'
        dst = dst_dir + "/" + file
        copyfile(src, dst)


#Develop baseline cnn

# baseline model for the dogs vs cats dataset


# define cnn model
def define_model():
	model = Sequential()
	model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same', input_shape=(200, 200, 3)))
	model.add(MaxPooling2D((2, 2)))
	model.add(Flatten())
	model.add(Dense(128, activation='relu', kernel_initializer='he_uniform'))
	model.add(Dense(1, activation='sigmoid'))
	# compile model
	opt = SGD(lr=0.001, momentum=0.9)
	model.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])
	return model

# plot diagnostic learning curves
def summarize_diagnostics(history):
	# plot loss
	pyplot.subplot(211)
	pyplot.title('Cross Entropy Loss')
	pyplot.plot(history.history['loss'], color='blue', label='train')
	pyplot.plot(history.history['val_loss'], color='orange', label='test')
	# plot accuracy
	pyplot.subplot(212)
	pyplot.title('Classification Accuracy')
	pyplot.plot(history.history['accuracy'], color='blue', label='train')
	pyplot.plot(history.history['val_accuracy'], color='orange', label='test')
	# save plot to file
	filename = sys.argv[0].split('/')[-1]
	pyplot.savefig(filename + '_plot.png')
	pyplot.close()

# run the test harness for evaluating a model
def run_test_harness():
	# define model
	model = define_model()
	# create data generator
	datagen = ImageDataGenerator(rescale=1.0/255.0)
	# prepare iterators
	train_it = datagen.flow_from_directory('Data/train',
		class_mode='binary', batch_size=64, target_size=(200, 200))
	test_it = datagen.flow_from_directory('Data/test/',
		class_mode='binary', batch_size=64, target_size=(200, 200))
	# fit model
	history = model.fit_generator(train_it, steps_per_epoch=len(train_it),
		validation_data=test_it, validation_steps=len(test_it), epochs=20, verbose=0)
	# evaluate model
	_, acc = model.evaluate_generator(test_it, steps=len(test_it), verbose=0)
	print('> %.3f' % (acc * 100.0))
	# learning curves
	summarize_diagnostics(history)

# entry point, run the test harness
run_test_harness()