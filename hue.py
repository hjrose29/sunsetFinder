
from webbrowser import get
from PIL import Image
import colorsys

def get_dominant_hue(filename):
    # Open the image file
    image = Image.open(filename)

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


sunset = "/Users/henry/Documents/sunsetFinder/Data/trainNew/Sunsets/20210206-1725.jpg"
nonsunset = "/Users/henry/Documents/sunsetFinder/Data/trainNew/Non-Sunsets/20210224-1740.jpg"
