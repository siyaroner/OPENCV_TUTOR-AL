import cv2 as cv

            #Reading images

img=cv.imread("data/photos/kitten1.jpg")

cv.imshow("kitten",img)

cv.waitKey(0)

img=cv.imread("data/photos/kitten3.jpg") #this pic size is large so it will go off the screen Therefore we're gona resize it later

cv.imshow("kitten",img)

cv.waitKey(0)

            #Reading Videos
            
# capture=cv.VideoCapture(0) #to use laptop webcam. If you wanna use external camera you have to type 1,2 etc
# while True: #we need a loop to read a video frame by frame
#     isTrue,frame=capture.read()
#     cv.imshow("Camera",frame)
#     if cv.waitKey(20) & 0xFF==ord("d"):
#         break
# capture.release()
# cv.destroyAllWindows()

# capture=cv.VideoCapture("data/videos/kitten.mp4") 
# while True: #we need a loop to read a video frame by frame
#     isTrue,frame=capture.read()
#     cv.imshow("Kitten",frame)
#     if cv.waitKey(50) & 0xFF==ord("q"): #if video is shorter than 50 seconds or we give wrong path it will give -215 assertion failed
#         break
# capture.release()
# cv.destroyAllWindows()
