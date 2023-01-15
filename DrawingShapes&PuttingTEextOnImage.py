import cv2 as cv
import numpy as np

##--- create blank images
blank=np.zeros((500,500,3),dtype="uint8")
# cv.imshow("Blank",blank)
# img=cv.imread("data/photos/kitten1.jpg")
# cv.imshow("Kitten",img)

##--- Point the image a certain colour
# blank[:]=0,255,0 #this will create a green image
# cv.imshow("Grean",blank)
# blank[:]=0,0,255 #this will create a red image
# cv.imshow("Red",blank)
# blank[:,0:250]=0,0,255 #this will create a red image
# blank[:,250::]=255,255,255 #this will create a red image
# cv.imshow("Turkey",blank)

## --- Drawing a rectangle
# cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,10),thickness=2)
cv.rectangle(blank,(200,200),(300,300),(0,255,10),thickness=2)
## ---- drawing a circle
cv.circle(blank,(250,250),5,color=(0,0,255),thickness=-1) # -1 or cv.FILLED will fill the area of specified
cv.line(blank,(250,250),(250,300),color=(0,0,255),thickness=1)
## --- Adding text on image
cv.putText(blank,"Reticle",(150,400),cv.FONT_HERSHEY_TRIPLEX,2.0,(0,0,255), 2)      
cv.imshow("Rectangle",blank)
cv.waitKey(0)