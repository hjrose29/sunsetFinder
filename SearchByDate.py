import json
from datetime import datetime

filepath = "/Users/tristanallen/PycharmProjects/SunsetFinder/archive.json"


def search(date):
    # load json file
    with open(filepath, 'r') as file:
        data = json.load(file)
    data_array = data['test']

    # initialize variables
    closest_date = None
    matches = []

    # create date time object YYYY-MM-DD
    input_date_object = datetime.strptime(formatted_date, '%Y-%m-%d')

    # traverse the json file and look for any matches
    for json_object in data_array:
        extracted_date = json_object.get('date_taken')
        file_date_object = datetime.strptime(extracted_date, '%Y-%m-%d')  # create date time object YYYY-MM-DD
        if date == extracted_date:  # match found
            matches.append(json_object)  # add the whole json object
        elif closest_date is None or abs(file_date_object - input_date_object) < abs(closest_date - input_date_object):
            closest_date = file_date_object
    if matches:
        return matches
    elif closest_date is not None:
        return search(closest_date)  # search again on the closest date found
    else:
        return None


# take user input and format to YYYY-MM-DD
input_date = " "
try:
    input_date = input("Enter a date... ")
    month, day, year = input_date.split('/')
    formatted_date = year + "-" + month + "-" + day

    if search(formatted_date) is not None:
        print(search(formatted_date))
    else:
        print("No file found for: " + input_date)
except ValueError:
    print(input_date + " is not a valid input. Enter a date MM/DD/YYYY")
