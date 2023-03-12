#HSV (HUE, Saturation, Value) for more see   data/notes/hsv.png
import cv2 as cv
import numpy as np

def nothing ():
    pass

cv.namedWindow("Tracking")

while True:
    frame =cv.imread("data/photos/trafficlight.jpg")
    cv.imshow("frame",frame)
    key=cv.waitKey( )
    if key==ord(" "):
        break
cv.destroyAllWindows()

