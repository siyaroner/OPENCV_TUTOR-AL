import cv2 as cv

img=cv.imread("data/photos/ayasofyacami.jpg")
cv.imshow("AyasofyaCami",img)

## Averaging

average=cv.blur(img,(5,5))
cv.imshow("Average Blur",average)

#Gaussian Blur
gauss=cv.GaussianBlur(img,(5,5),1.5)
cv.imshow("Gaussian Blur",gauss)

gauss=cv.GaussianBlur(img,(5,5),0)
cv.imshow("Gaussian Blur variance 0",gauss)

## Median Blur
median=cv.medianBlur(img,5)
cv.imshow("Median Blur",median)

## Bilateral Blur
bilateral=cv.bilateralFilter(img,50,100,100)
cv.imshow("Bilateral Blur",bilateral)
cv.waitKey( )
cv.destroyAllWindows()