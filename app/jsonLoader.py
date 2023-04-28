import json
import os
from ImageToString import *
path = "app/archive.json"

def clearJson():

    os.remove(path)
    with open(path, 'w') as f:
        f.write("{\n\t\"test\": [\n\t]\n}")

def getImages(jsonPath):
    out = []
    f = open(jsonPath)

    data = json.load(f)
    count = 1
    first = []
    second = []
    third = []
    fourth = []
    for i in data["test"]:
        if(count % 4 == 0):
            fourth.append(i["image_name"])
        
        elif(count % 3 == 0):
            third.append(i["image_name"])
        elif(count % 2 == 0):
            
            second.append(i["image_name"])
        else:
            first.append(i["image_name"])
    out.append(first)
    out.append(second)
    out.append(third)
    out.append(fourth)
    return out

    

def getDates(jsonPath):
    out = []
    f = open(jsonPath)

    data = json.load(f)
    for i in data["test"]:
        out.append(i["date_taken"])

    return out

def fillPicturesToDisplay():
    for i in os.listdir("/Users/henry/Documents/sunsetFinder/Data/Sunsets"):
        resizeImage("/Users/henry/Documents/sunsetFinder/Data/Sunsets/", i, "/Users/henry/Documents/sunsetFinder/app/picturesToDisplay/" + i)

def fillJson(displayFolderPath):
    date = 0
    for i in os.listdir(displayFolderPath):
        date += 1
        update_json(file_to_base64(displayFolderPath + i),date)

