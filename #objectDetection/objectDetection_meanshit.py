import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#read video
cap = cv.VideoCapture(r'C:\Users\amora\OneDrive\Documents\Visual Studio Code\Course_Imageproccesing2\videos\file slow.flv in open cv.mp4')

#____________________________________________step 1___________________________________________________#
#read first frame
ret , frame = cap.read()
#Enter first pos of obj
x ,y ,w , h =  300 , 200 , 100 , 50
trackWindow = (x,y,w,h)
#set up roi
roi = frame[y:y+h , x:x+w]


#____________________________________________step 2___________________________________________________#
#convert roi to hsv
hsv_roi = cv.cvtColor(roi , cv.COLOR_BGR2HSV)
#MAKE IN_RANGE with mask
mask = cv.inRange(hsv_roi , np.array((0.,60.,32.)) , np.array((180.,255.,255)))
#get histogram
hist_roi = cv.calcHist([hsv_roi] , [0] , mask , [180] , [0,180] )
# normalize histogram
normalize_roi = cv.normalize(hist_roi , hist_roi , 0 , 180 , cv.NORM_MINMAX)
#cal criteria
criteria = ( cv.TERM_CRITERIA_EPS |  cv.TERM_CRITERIA_COUNT , 10 , 1)

#____________________________________________step 3___________________________________________________#
while cap.isOpened() :
    
    #read frame
    ret , frame = cap.read()
    #convert it to hsv
    hsv_frame = cv.cvtColor(frame ,  cv.COLOR_BGR2HSV)
    #now get back projection
    backProject = cv.calcBackProject([hsv_frame] , [0] , hist_roi , [0,180] ,1 )
    #apply mean_shit
    ret , trackWindow = cv.meanShift(backProject , trackWindow , criteria)

    #get values from track_window
    x,y,w,h = trackWindow
    final_image = cv.rectangle(frame , (x,y) , (x+w,y+h) , (0,255,0) , 2 )


    #show image
    cv.imshow("original" , frame)
    cv.imshow("meanShift" , final_image)

    if cv.waitKey(1) & 0xFF == ord('q') :
        break

        
cv.destroyAllWindows()
cap.release()    
