import cv2 as cv
from datetime import datetime

cap=cv.VideoCapture(0)
#print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
#print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
#cap.set(3,3000) #3 assosiate with cv.CAP_PROP_FRAME_WIDTH
#cap.set(4,3000) #4 assosiate with cv.CAP_PROP_FRAME_HEIGHT


#taking a pic&vid and put current time on them
while (cap.isOpened()):
    T_or_F,frame=cap.read()
    
    if T_or_F is True:
        font=cv.FONT_HERSHEY_SCRIPT_SIMPLEX
        text=str(datetime.now())
        frame=cv.putText(frame,text,(200,475),font,1,(0,0,255),2)
        cv.imshow("frame",frame)
        if cv.waitKey(20) & 0xFF==ord(" "):
            pic=cv.imwrite("capture.jpg",frame)
            break
    
cap.release()
cv.destroyAllWindows()
# cv.waitKey( )