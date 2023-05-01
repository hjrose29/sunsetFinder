import json
from datetime import datetime

filepath = "/Users/henry/Documents/sunsetFinder/app/archive.json"


def search(date, jsonPath):

    # load json file
    with open(jsonPath, 'r') as file:
        data = json.load(file)
    data_array = data['test']

    # initialize variables
    closest_date = None
    matches = []

    # create date time object YYYY-MM-DD
    input_date_object = datetime.strptime(date, '%Y-%m-%d')
    count = 0
    # traverse the json file and look for any matches
    for json_object in data_array:
        extracted_date = json_object.get('date_taken')
        month, day, year = extracted_date.split('/')
        extracted_date = year + "-" + month + "-" + day
        file_date_object = datetime.strptime(extracted_date, '%Y-%m-%d')  # create date time object YYYY-MM-DD
        if date == extracted_date:  # match found
            matches.append(json_object)  # add the whole json object
            count += 1
        elif closest_date is None or abs(file_date_object - input_date_object) < abs(closest_date - input_date_object):
            closest_date = file_date_object
    if matches:
        return matches
    elif closest_date is not None:
        closest_date = closest_date.strftime('%Y-%m-%d')
        return search(closest_date)  # search again on the closest date found
    else:
        return None


    
    