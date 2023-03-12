#HSV (HUE, Saturation, Value) for more see   data/notes/hsv.png
import cv2 as cv
import numpy as np

def nothing (x):
    pass

cv.namedWindow("Tracking")
cv.createTrackbar("LH","Tracking",0,255,nothing) #LH lower hue
cv.createTrackbar("LS","Tracking",0,255,nothing) #lower saturation
cv.createTrackbar("LV","Tracking",0,255,nothing) #lower value
cv.createTrackbar("UH","Tracking",255,255,nothing) #upper hue
cv.createTrackbar("US","Tracking",255,255,nothing) #upper saturation
cv.createTrackbar("UV","Tracking",255,255,nothing) #upper value


while True:
    frame =cv.imread("data/photos/trafficlight.jpg")
    # _,frame=cv.read()
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    # l_r=np.array([140,140,20])
    # u_r=np.array([255,255,255])
    
    l_h=cv.getTrackbarPos("LH","Tracking")
    l_s=cv.getTrackbarPos("LS","Tracking")
    l_v=cv.getTrackbarPos("LV","Tracking")
    
    u_h=cv.getTrackbarPos("UH","Tracking")
    u_s=cv.getTrackbarPos("US","Tracking")
    u_v=cv.getTrackbarPos("UV","Tracking")
        
    l_r=np.array([l_h,l_s,l_v])
    u_r=np.array([u_h,u_s,u_v])
    print(l_r,u_r)
    mask=cv.inRange(hsv,l_r,u_r)
    res=cv.bitwise_and(frame,frame,mask=mask)
    
    cv.imshow("frame",frame)
    cv.imshow("mask",mask)
    cv.imshow("res",res)
    
    key=cv.waitKey(1)
    if key==ord(" "):
        break

# cap.release()
cv.destroyAllWindows()

