import json

path = "app/archive.json"

   
def getImages(jsonPath):
    out = []
    f = open(jsonPath)

    data = json.load(f)
    for i in data["test"]:
        out.append(i["image_name"])

    return out

def getDates(jsonPath):
    out = []
    f = open(jsonPath)

    data = json.load(f)
    for i in data["test"]:
        out.append(i["date_taken"])

    return out
