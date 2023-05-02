
import datetime
from vidgear.gears import CamGear
import cv2
from PIL import Image
import time
saveDirectory = "/Users/henry/Documents/sunsetFinder/toDisplay/"

stream = CamGear(source='https://www.youtube.com/embed/wfhQTU0HrpY', stream_mode = True, logging=True).start() # 

while True:
    frame = stream.read()
    # read frames
    now = datetime.datetime.now()

    current_date = now.strftime("%Y%m%d")
    current_time = now.strftime("%H:%M")
    imgName = current_date + "-" + current_time
    cv2.imwrite(saveDirectory + imgName + ".jpg", frame)
    time.sleep(60)

    
