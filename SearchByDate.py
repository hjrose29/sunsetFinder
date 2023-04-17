import os
from datetime import datetime

filepath = "/Users/tristanallen/PycharmProjects/SunsetFinder/sunset"


# search for the input date, or find the closest date
def search(date):
    closest_date = None
    closest_filename = None
    matches = []
    input_date_object = datetime.strptime(formatted_date, '%Y%m%d')
    for filename in os.listdir(filepath):
        formatted_file = format_file(filename)
        file_date_object = datetime.strptime(formatted_file, '%Y%m%d')
        if date == formatted_file:
            matches.append(filename)
        elif closest_date is None or abs(file_date_object - input_date_object) < abs(closest_date - input_date_object):
            closest_date = file_date_object
            closest_filename = filename
    if matches:
        return matches
    elif closest_date is not None:
        return search(format_file(closest_filename))
    else:
        return None


def format_file(file):
    return file.split('-')[0]


# take input and format to YYYYMMDD
input_date = input("Enter a date... ")
month, day, year = input_date.split('/')
formatted_date = year + month + day

if search(formatted_date) is not None:
    print(search(formatted_date))
else:
    print("No file found for: " + input_date)
