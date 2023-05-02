import os

import cv2
import numpy as np

filepath = "/Users/tristanallen/PycharmProjects/SunsetFinder/TestPictures/"


def detect_sunset(picture):
    # set color ranges for sunset detection
    lower = np.array([5, 50, 50])
    upper = np.array([25, 255, 255])

    image = cv2.imread(filepath + picture)

    # apply color filter
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # convert to hsv
    mask = cv2.inRange(hsv, lower, upper)  # mask for only the color range specified
    # cv2.bitwise_and(image, image, mask=mask)

    # calculate percentage of sunset pixles
    percent_sunset = np.count_nonzero(mask) / mask.size * 100

    # save image to either sunset or not_sunset
    if percent_sunset > 10:
        cv2.imwrite(os.path.join('sunset', picture), image)
    else:
        cv2.imwrite(os.path.join('not_sunset', picture), image)

    # check if the directories exist
    if not os.path.exists('sunset'):
        os.mkdir('sunset')
    if not os.path.exists('not_sunset'):
        os.mkdir('not_sunset')


for pic in os.listdir('TestPictures'):
    detect_sunset(pic)
