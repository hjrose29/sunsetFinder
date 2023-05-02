import os
import shutil

import cv2
import numpy as np

filepath = "/Users/henry/Documents/sunsetFinder/Data/trainNew/"
S = "Sunsets/"
N = "Non-Sunsets/"


def detect_sunset(path, picture):
    # set color ranges for sunset detection
    lower = np.array([5, 50, 50])
    upper = np.array([25, 255, 255])

    image = cv2.imread(path + picture)

    # apply color filter
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # convert to hsv
    mask = cv2.inRange(hsv, lower, upper)  # mask for only the color range specified
    # cv2.bitwise_and(image, image, mask=mask)

    # calculate percentage of sunset pixles
    percent_sunset = np.count_nonzero(mask) / mask.size * 100

    # save image to either sunset or not_sunset
    if percent_sunset > 10:
        cv2.imwrite("/Users/henry/Documents/sunsetFinder/algoSays/" + picture, image)

c = 0
tc = 0

def isSunset(img):
    out = False
    lower = np.array([5, 50, 50])
    upper = np.array([25, 255, 255])
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # convert to hsv
    mask = cv2.inRange(hsv, lower, upper)
    percent_sunset = np.count_nonzero(mask) / mask.size * 100
    if percent_sunset > 35:
        out = True

    return out



# for i in os.listdir(filepath + S):
#     if(i == ".DS_Store"):
#         continue
#     lower = np.array([5, 50, 50])
#     upper = np.array([25, 255, 255])
#     image = cv2.imread(filepath + S + i)
#     hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # convert to hsv
#     mask = cv2.inRange(hsv, lower, upper)  # mask for only the color range specified
#     percent_sunset = np.count_nonzero(mask) / mask.size * 100
#     tc += 1
#     if percent_sunset > 35:
#         c += 1


# c2 = 0
# tc2 = 0

# for i in os.listdir(filepath + N):
#     if(i == ".DS_Store"):
#         continue
#     lower = np.array([5, 50, 50])
#     upper = np.array([25, 255, 255])
#     image = cv2.imread(filepath + N + i)
#     hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # convert to hsv
#     mask = cv2.inRange(hsv, lower, upper)  # mask for only the color range specified
#     percent_sunset = np.count_nonzero(mask) / mask.size * 100
#     tc2 += 1
#     if percent_sunset > 35:
#         c2 += 1


# path = "/Users/henry/Documents/sunsetFinder/toSplit/"

# for i in os.listdir(path):
#     if(i == ".DS_Store"):
#         continue
#     lower = np.array([5, 50, 50])
#     upper = np.array([25, 255, 255])
#     image = cv2.imread(path + i)
#     hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # convert to hsv
#     mask = cv2.inRange(hsv, lower, upper)  # mask for only the color range specified
#     percent_sunset = np.count_nonzero(mask) / mask.size * 100
#     if percent_sunset > 35:
#         shutil.copyfile(path + i, "/Users/henry/Documents/sunsetFinder/algoSays/" + i)


    

    
