
import os
import shutil
from webbrowser import get
from PIL import Image
import colorsys
import numpy as np
from app.ImageToString import resize, resizeImage
import numpy
##For CV2
def get_hue(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hue = np.mean(hsv[:,:,0])
    return hue

def pathHue(path):
    img = resize(path)
    center = img.shape
    x = center[1]/2 - w/2
    y = center[0]/2 - h/2  
    crop_img = img[int(y):int(y+h), int(x):int(x+w)]
    
    return get_hue(crop_img)

#for Pillow
def get_dominant_hue():
    # Open the image file
    image = img

    # Convert the image to HSV color space
    hsv_image = image.convert('HSV')

    # Get the hue statistics of the image
    hue_data = hsv_image.histogram()[128:256]

    # Calculate the dominant hue of the image
    max_hue = max(hue_data)
    max_hue_index = hue_data.index(max_hue)
    dominant_hue = (max_hue_index + 128) / 255.0

    # Return the dominant hue of the image
    return dominant_hue

trainDataPath = "/Users/henry/Documents/sunsetFinder/Data/trainNew/"
S = "Sunsets/"
N = "Non-Sunsets/"


import cv2

h=125
w=200



# img = resize("/Users/henry/Documents/sunsetFinder/Data/trainNew/Sunsets/good_20200903-1927.jpg")

# center = img.shape
# x = center[1]/2 - w/2
# y = center[0]/2 - h/2
# crop_img = img[int(y):int(y+h), int(x):int(x+w)]
# cv2.imshow("cropped", crop_img)
# cv2.waitKey(0)


sunsetHues = []
for i in os.listdir(trainDataPath + S):
    if(i == ".DS_Store"):
        continue
    ###Get center of image
    img = resize(trainDataPath + S + i)
    center = img.shape
    x = center[1]/2 - w/2
    y = center[0]/2 - h/2  
    crop_img = img[int(y):int(y+h), int(x):int(x+w)]

    ####Get Hue
    sunsetHues.append(get_hue(crop_img))

nonSunsetHues = []
for i in os.listdir(trainDataPath + N):
    if(i == ".DS_Store"):
        continue
    ###Get center of image
    img = resize(trainDataPath + N + i)
    center = img.shape
    x = center[1]/2 - w/2
    y = center[0]/2 - h/2  
    crop_img = img[int(y):int(y+h), int(x):int(x+w)]

    ####Get Hue
    nonSunsetHues.append(get_hue(crop_img))



# def avg(listOfNumbers):
#     sum = 0
#     for i in listOfNumbers:
#         sum += i
#     return sum / len(listOfNumbers)

from matplotlib import pyplot as plt
plt.subplots(1,2)
plt.boxplot(sunsetHues)
plt.boxplot(nonSunsetHues)



sunsetHues = np.array(sunsetHues)
nonSunsetHues = np.array(nonSunsetHues)

print("Sunsets - Non Sunsets")
print("Min:    " + str(numpy.min(sunsetHues)) + " - " + str(numpy.min(nonSunsetHues)))
print("Max:    " + str(numpy.max(sunsetHues)) + " - " + str(numpy.max(nonSunsetHues)))
print("90th %: " + str(numpy.quantile(sunsetHues, .90)) + " - " + str(numpy.quantile(nonSunsetHues, .90)))
print("Mean:   " + str(numpy.mean(sunsetHues)) + " - " + str(numpy.mean(nonSunsetHues)))
print("Median: " + str(numpy.median(sunsetHues)) + " - " + str(numpy.median(nonSunsetHues)))


