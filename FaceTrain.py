import os
import cv2 as cv
import numpy as np

celebrities=[] # ['Brad Pitt', 'Dwayne Johnson', 'Henry Cavill', 'Robert Downey Jr', 'Tom Cruise']
j=0
for i in os.listdir(r"D:\DataScienceTutorial\data\FaceRecognition\Faces\train"):
    celebrities.append(i)
    j+=1
    if j==5:
        break
# print(celebrities)
DIR=r"D:\DataScienceTutorial\data\FaceRecognition\Faces\train"

haar_cascade=cv.CascadeClassifier("haar_face.xml")

features=[]
labels=[]

def create_train():
    for person in celebrities:
        path=os.path.join(DIR,person)
        label=celebrities.index(person)
        
        for img in os.listdir(path):
            img_path=os.path.join(path,img)

            img_array=cv.imread(img_path)
            if img_array is None:
                continue
            
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            
            faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
            
            for (x,y,w,h) in faces_rect:
                faces_roi=gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print(len(features),len(labels))
print(" Training is done...")
features=np.array(features,dtype="object")
labels=np.array(labels)

face_recognizer=cv.face.LBPHFaceRecognizer_create()

# Train the REcognizer on the features list and the labels list

face_recognizer.train(features,labels)

face_recognizer.save("face_trained.yml")
np.save("features.npy",features)
np.save("labels.npy",labels)



cv.waitKey( )
cv.destroyAllWindows()


