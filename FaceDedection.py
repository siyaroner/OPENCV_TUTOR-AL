import cv2 as cv

# img=cv.imread("data/photos/success_kid.jpg")
# cv.imshow("success_kid",img)

# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("gray",gray)

# haar_cascade=cv.CascadeClassifier("haar_face.xml")

# face_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
# print(f"number of faces found= {len(face_rect)}")

# for (x,y,w,h) in face_rect:
#     cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
# cv.imshow("detected faces",img)

kids=cv.imread("data/photos/kids.jpg")
cv.imshow("kids",kids)

gray_kids=cv.cvtColor(kids,cv.COLOR_BGR2GRAY)
cv.imshow("gray_kids",gray_kids)

haar_cascade=cv.CascadeClassifier("haar_face.xml")
face_rect=haar_cascade.detectMultiScale(gray_kids,scaleFactor=1.2,minNeighbors=2)
print(f"number of faces found= {len(face_rect)}")

for (x,y,w,h) in face_rect:
    cv.rectangle(kids,(x+10,y+10),(x+w- 10,y+h),(0,255,0),thickness=2)

cv.imshow("face detected",kids)

cv.waitKey( )
cv.destroyAllWindows()