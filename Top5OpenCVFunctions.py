import cv2 as cv
import numpy as np

kernel= np.ones((5,5),np.uint8)

path="data/photos/kitten2.jpg"

img=cv.imread(path)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur=cv.GaussianBlur(gray,(7,7),0)
canny=cv.Canny(blur,100,200)
dilation=cv.dilate(canny,kernel,iterations=4)
eroded=cv.erode(dilation,kernel,iterations=2)

cv.imshow("kitten",img)
cv.imshow("gray",gray)
cv.imshow("blur",blur)
cv.imshow("eroded",eroded)
cv.imshow("canny",canny)
cv.imshow("dilation",dilation)

cv.waitKey( )
cv.destroyAllWindows()