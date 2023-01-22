import cv2 as cv
import numpy as np

img=cv.imread("data/photos/kitten1.jpg")
cv.imshow("kitten",img)

cv.wiatKey( )
cv.destroyAllWindows()