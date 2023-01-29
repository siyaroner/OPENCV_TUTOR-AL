import cv2 as cv
import numpy as np

bugatti=cv.imread("data/photos/bugatti.jpg")
cv.imshow("bugatti",bugatti)

gray=cv.cvtColor(bugatti,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

# #laplacian
# lap=cv.Laplacian(gray,cv.CV_64F)
# lap=np.uint8(np.absolute(lap))
# cv.imshow("laplacian",lap)

# #SOBEL
# sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
# sobely=cv.Sobel(gray,cv.CV_64F,0,1)
# combined_sobel=cv.bitwise_or(sobely,sobelx)
# cv.imshow("sobalx",sobelx)
# cv.imshow("sobaly",sobely)
# cv.imshow("combined_sobel",combined_sobel)

canny=cv.Canny(gray,220,255)
cv.imshow("canny",canny)
cv.waitKey( )
cv.destroyAllWindows()