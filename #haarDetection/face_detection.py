import cv2 as cv
import numpy as np

#read_video
cap = cv.VideoCapture(0)

#image
# img = cv.imread(r'C:\Users\amora\OneDrive\Documents\Visual Studio Code\Course_Imageproccesing2\photos\lady.jpg')
# gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

#read cascade
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade  = cv.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

#function that do cascade
def cascade_process(frame , gray) :
    #get faces
    faces = face_cascade.detectMultiScale(gray , 1.1 , 4)

    #loop on faces
    for x,y,w,h in faces :
        #draw rect on face
        cv.rectangle(frame , (x,y) , (x+w , y+h) , (0,255,0) , 2  )
        #get roi of face with gray and color
        roi_gray = gray[y:y+h , x:x+w]
        roi_col = frame[y:y+h , x:x+w]
        #get eyes
        eyes = eye_cascade.detectMultiScale(roi_gray , 1.1 , 4)

        #loop on eyes
        for ex,ey,ew,eh in eyes :
            cv.rectangle(roi_col , (ex,ey) , (ex+ew , ey+eh) , (0,255,0) , 2  )

        return frame    


while cap.isOpened() :
    ret , frame = cap.read()

    #convert frame to gray
    gray = cv.cvtColor(frame , cv.COLOR_BGR2GRAY)

    #Pass frame to function
    frame = cascade_process(frame , gray)  

    #show frame
    cv.imshow('video' , frame)

    #break
    if cv.waitKey(1) & 0xFF == ord('q') :
        break

cap.release()
cv.destroyAllWindows()    