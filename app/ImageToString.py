from PIL import Image
import base64
from io import BytesIO
import os
import json, datetime

file_path = "/Users/henry/Documents/sunsetFinder/Data/train/Sunsets/20210221-1730.jpg"

def resizeImage(path, oldName, newName):

    
    old_path = path + oldName
    new_path = path + newName

    image = Image.open(old_path)
    image.thumbnail((250, 250))
    image.save(new_path)

def file_to_base64(file_path):
    with open(file_path, 'rb') as file:

        encoded = base64.b64encode(file.read())
        return encoded.decode('utf-8')



def update_json(image_name, date):
    # Load the JSON file
    with open("/Users/henry/Documents/sunsetFinder/app/archive.json", 'r') as f:
        data = json.load(f)

    # Parse the date string into a datetime object
    date_taken = date

    # Create a new object with the image name and date
    new_object = {'image_name': image_name, 'date_taken': date_taken}

    # Add the new object to the 'test' array
    data['test'].append(new_object)

    # Write the updated data back to the JSON file
    with open("/Users/henry/Documents/sunsetFinder/app/archive.json", 'w') as f:
        json.dump(data, f, indent=2)

# for i in os.listdir("/Users/henry/Documents/sunsetFinder/Data/Sunsets"):
#     if(i != "Thumbnails"):
#         resizeImage("/Users/henry/Documents/sunsetFinder/Data/Sunsets/", i, "Thumbnails/Thumbnail " + i)

#for i in os.listdir("/Users/henry/Documents/sunsetFinder/Data/Sunsets/Thumbnails"):
 #   update_json(file_to_base64("/Users/henry/Documents/sunsetFinder/Data/Sunsets/Thumbnails/" + i))


path = "/Users/henry/Documents/sunsetFinder/app/Data/Sunsets/"
name = "20210206-1710.jpg"
def toDisplayToJson(path, img_name):
     year = img_name[0:4]
     month = img_name[4:6]
     day = img_name[6:8]
     date = month + "/" + day + "/" + year
     encoded = file_to_base64(path + img_name)
     return encoded, date

        
