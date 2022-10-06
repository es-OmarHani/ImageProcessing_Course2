import cv2 as cv
import numpy as np

#read cap
cap = cv.VideoCapture(0)

#read 2 frames
ret , frame1 = cap.read()
ret , frame2 = cap.read()

while cap.isOpened() :

    #diff between 2 frames
    diff = cv.absdiff(frame1 , frame2)
    gray = cv.cvtColor(diff , cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray , (5,5) , 0)
    _ , thresh = cv.threshold(blur , 30 , 180 , cv.THRESH_BINARY )
    dilated = cv.dilate(thresh , None , iterations = 3 )
    # canny = cv.Canny(gray , 0 , 0)

    #find contours
    contours , _ = cv.findContours(dilated , cv.RETR_TREE , cv.CHAIN_APPROX_SIMPLE)

    for contour in contours :
        #get rect bounding of contours
        x , y , w , h = cv.boundingRect(contour)

        if cv.contourArea(contour) < 900 :
            continue

        cv.rectangle(frame1 , (x,y) , (x+w , y+h) , (0,255,0) , 3)
        # cv.putText()


    #show frame
    cv.imshow('video' , frame1)

    # get new read
    frame1 = frame2
    ret , frame2 = cap.read()

    #break video
    if cv.waitKey(1) & 0xFF == ord('q') :
        break

cap.release()
cv.destroyAllWindows()        
        

