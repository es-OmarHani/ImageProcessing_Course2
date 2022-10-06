import cv2 as cv
import numpy as np

#read image
img = cv.imread(r'C:\Users\amora\OneDrive\Documents\Visual Studio Code\Course_Imageproccesing2\photos\road1.jpg' , 0)
#canny detection
canny = cv.Canny(img , 150 , 200 , apertureSize = 3)
#lines using hough_lines
lines = cv.HoughLines(canny , 1 , np.pi/180 , 100)

#blank imag
blank = np.zeros((img.shape[:2]) , dtype='uint8')

# loop to get 2points of lines
for point in lines :
    # get rho and theta
    rho , theta = point[0]
    #get a , b 
    a = np.cos(theta)
    b = np.sin(theta)
    
    #get x0 , y0
    x0 = a * rho
    y0 = b * rho

    #get x1 , y1 point 1
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))

    #get x2 , y2 point 2
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    #draw line with 2 points
    cv.line(img , (x1,y1) , (x2,y2) , (255,255,255) , 1 )

#show image
cv.imshow('Road_Edges' , canny )
cv.imshow('Road' , img )

cv.waitKey(0)
cv.destroyAllWindows()
