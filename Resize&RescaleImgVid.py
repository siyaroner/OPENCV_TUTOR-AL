import cv2 as cv
import pygame

img=cv.imread("data/photos/kitten3.jpg") #this pic size is large so it will go off the screen Therefore we're gona resize it later
# cv.imshow("kitten",img)
# cv.waitKey(0)
##Resacele
pygame.init()
screensize=pygame.display.list_modes()
screen_width=screensize[0][0]
screen_height=screensize[0][1]

scale_width=screen_width/img.shape[1]
scale_height=screen_height/img.shape[0]

def rescaleFrame(frame,scale=0.50):
    width=int(frame.shape[1]*scale_width)
    height=int(frame.shape[0]*scale_height)
    print(height)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

img_rescaled=rescaleFrame(img)
cv.imshow("kitten3 rescaled",img_rescaled)
cv.waitKey(0)