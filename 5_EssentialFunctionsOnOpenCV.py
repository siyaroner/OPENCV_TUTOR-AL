import cv2 as cv
img=cv.imread("data/photos/kitten1.jpg")
cv.imshow("Kitten_normal",img)

##converting bgr image to grayscale image
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("Kitten_gray",gray)

##Blur
# blur=cv.GaussianBlur(img,(9,9),cv.BORDER_DEFAULT)
# cv.imshow("Blur",blur)

## Edge Cascade
# canny=cv.Canny(img,125,175)
# cv.imshow("Canny",canny)
# canny_blur=cv.Canny(blur,125,175) #to reduce edges we can blured image
# cv.imshow("Canny_Blur",canny_blur)

#Dilating the image
# dilated=cv.dilate(canny,(7,7),iterations=4) #the lines will be thicker
# cv.imshow("dilated",dilated)

#Eroding the image
# eroded=cv.erode(dilated,(7,7),iterations=4) #the lines will be thicker
# cv.imshow("Eroded",eroded)

##Resize the image
# reduce_dimensions=cv.resize(img,(150,150),interpolation=cv.INTER_AREA) #when you shirink the image use INTER_AREA
# cv.imshow("resized",reduce_dimensions)
# enlarge_dimensions=cv.resize(img,(750,750),interpolation=cv.INTER_CUBIC) #when you shirink the image use INTER_CUBIC OR INTER_LINEAR ( CUBIC is slower)
# cv.imshow("enlarge",enlarge_dimensions)

## croping
cropped=img[50:100,100:200]
cv.imshow("cropped",cropped)
cv.waitKey(0)




