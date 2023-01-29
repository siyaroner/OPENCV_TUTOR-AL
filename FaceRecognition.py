import os
import cv2 as cv
import numpy as np

haar_cascade=cv.CascadeClassifier("haar_face.xml")

celebrities=[] # ['Brad Pitt', 'Dwayne Johnson', 'Henry Cavill', 'Robert Downey Jr', 'Tom Cruise']
j=0
for i in os.listdir(r"D:\DataScienceTutorial\data\FaceRecognition\Faces\train"):
    celebrities.append(i)
    j+=1
    if j==5:
        break
print(celebrities)

features=np.load("features.npy",allow_pickle=True)
labels=np.load("labels.npy")

face_recognizer=cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("face_trained.yml")

img=cv.imread(r"D:\DataScienceTutorial\data\FaceRecognition\Faces\train\Brad Pitt\Brad Pitt_12.jpg")

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

#Detect the face in the image

face_rect=haar_cascade.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in face_rect:
    face_roi=gray[y:y+h,x:x+w]
    
    label,confidence=face_recognizer.predict(face_roi)
    print(f"label={celebrities[label]} with a confidence of {confidence}")
    
    cv.putText(img,str(celebrities[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow("Detected Face", img)


cv.waitKey( )
cv.destroyAllWindows()
