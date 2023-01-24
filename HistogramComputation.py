import cv2 as cv

img=cv.imread("data/photos/ayasofyacami.jpg")
cv.imshow("ayasofyacami",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

cv.waitKey( )
cv.destroyAllWindows()