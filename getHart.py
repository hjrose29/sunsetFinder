
from vidgear.gears import CamGear
import cv2
import shutil

saveDirectory = "/home/hrose3/sunsetFinder/sunsetFinder/unfiltered"

stream = CamGear(source='https://www.youtube.com/embed/wfhQTU0HrpY', stream_mode = True, logging=True).start() # 

while True:
    frame = stream.read()
    # read frames

    # check if frame is None
    if frame is None:
        #if True break the infinite loop
    cv2.imwrite(saveDirectory, frame)
    
