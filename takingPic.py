import cv2
from cropping import *

videoCaptureObject = cv2.VideoCapture(0)
while(True):
    ret,frame = videoCaptureObject.read()
    cv2.imshow('Capturing Video',frame)
    name = ""
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        name += "Test"
        name += ".jpg"
        cv2.imwrite(name,frame)
        break
videoCaptureObject.release()

cv2.destroyAllWindows()

cropper()

