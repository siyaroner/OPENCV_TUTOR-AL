import cv2 as cv
import numpy as np

img=cv.imread("data/photos/kitten1.jpg")
cv.imshow("img",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

## Simple Thresholding
# threshold,thresh=cv.threshold(gray,195,255,cv.THRESH_BINARY)
# cv.imshow("threshold",thresh)

# threshold,thresh_inv=cv.threshold(gray,195,255,cv.THRESH_BINARY_INV)
# cv.imshow("threshold",thresh_inv)

# ## Adaptive Thresholding
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow("adaptive_threshold",adaptive_thresh)

adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,3)
cv.imshow("adaptive_threshold",adaptive_thresh)

# adaptive_thresh_inv=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,3)
# cv.imshow("adaptive_threshold_inv",adaptive_thresh_inv)

cv.waitKey( )
cv.destroyAllWindows()