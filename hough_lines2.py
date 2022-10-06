import cv2 as cv
import numpy as np

#read image
img = cv.imread(r'C:\Users\amora\OneDrive\Documents\Visual Studio Code\Course_Imageproccesing2\photos\road1.jpg' , 0)
#canny detection
canny = cv.Canny(img , 100 , 150 )
#lines using hough_lines
lines = cv.HoughLinesP(canny , 1 , np.pi /180 , 100 , minLineLength = 150 , maxLineGap = 10)

# loop to get 2points of lines
for point in lines :
    print(point[0])
    # get x1,y1 and x2,y2
    x1 , y1 , x2 , y2 = point[0]
    # draw line with 2 points
    cv.line(img , (x1,y1) , (x2,y2) , (0,255,0) , 1 )

#show image
cv.imshow('Road_Edges' , canny )
cv.imshow('Road' , img )

cv.waitKey(0)
cv.destroyAllWindows()
