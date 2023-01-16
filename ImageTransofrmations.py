import cv2 as cv

img=cv.imread("data/photos/kitten1.jpg")
cv.imshow("Kitten",img)

#Translation
def translate(img,w,h):
    transMat=np.float32([[1,0,w],[0,1,h]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)
# -x -> left
# -y -> up
# x->right
# y ->down
translated=translate(img,100,200)
cv.imshow("Translatedtranslate")   
cv.waitKey(0)
cv.destroyAllWindows()
