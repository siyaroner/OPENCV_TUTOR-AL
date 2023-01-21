import cv2 as cv
import numpy as np

img=cv.imread("data/photos/kitten1.jpg")
cv.imshow("Kitten",img)

# #Translation
# def translate(img,x,y):
#     transMat=np.float32([[1,0,x],[0,1,y]])
#     dimensions=(img.shape[1],img.shape[0])
#     return cv.warpAffine(img,transMat,dimensions)
# # -x -> left
# # -y -> up
# # x->right
# # y ->down
# # translated=translate(img,50,50)
# translated=translate(img,-50,-50)

# cv.imshow("Translatedtranslate",translated)   

 
#  # Rotation
 
# def rotate (img,angle,rotPoint=None):
#     (height,width)=img.shape[:2]
#     if rotPoint is None:
#         rotPoint=(width//2,height//2)
#     rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
#     dimensions=(width,height)
#     return cv.warpAffine(img,rotMat,dimensions)
# rotated=rotate(img,180)
# cv.imshow("Rotated",rotated)


# ## Resizing

# resized=cv.resize(img,(250,250),interpolation=cv.INTER_CUBIC)
# cv.imshow("Resized",resized)


# ## Flipping
# flip=cv.flip(img,-1) #0: Vertically, 1:horizantally, -1:vertically and horizantally
# cv.imshow("Flipped",flip)

# cropping
cropped=img[100:200,200:300]
cv.imshow("Cropped",cropped)
cv.waitKey( )
cv.destroyAllWindows()