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
# works for videos,images, live videos
    width=int(frame.shape[1]*scale_width)
    height=int(frame.shape[0]*scale_height)
    print(height)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def changeRes(width,height):
# Only works for live videos
    capture.set(3,width)
    capture.set(4,height)

# img_rescaled=rescaleFrame(img)
# cv.imshow("kitten3 rescaled",img_rescaled)
# cv.waitKey(0)

#Reading Videos
capture=cv.VideoCapture(0)
while True:
    isTrue,frame=capture.read()
    resized_frame=rescaleFrame(frame)
    changeRes(500,144)
    cv.imshow("Camera",frame)
    cv.imshow("Camera2",resized_frame)
    # cv.imshow("Camera2",reres_frame)

    
    if cv.waitKey(20)&0xFF==ord("q"):
        break
capture.release()
cv.destroyAllWindows()
