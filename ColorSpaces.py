import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread("data/photos/kitten1.jpg")
cv.imshow("kitten",img)
plt.imshow(img) #opencv is bgr and plt is rgb so when you run this plt will convert b to r and r to b
plt.show()
# # BGR to grayscale
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("gray",gray)

# #BGR to hsv
# hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
# cv.imshow("hsv",hsv)
# #BGR to lab
# lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
# cv.imshow("lab",lab)

#BGR to RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
plt.imshow(rgb)
plt.show()
cv.waitKey( )
cv.destroyAllWindows()