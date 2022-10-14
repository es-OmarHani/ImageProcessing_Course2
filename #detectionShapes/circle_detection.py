import cv2 as cv
import numpy as np

# read img
img = cv.imread(r'C:\Users\amora\OneDrive\Documents\Visual Studio Code\Course_Imageproccesing2\photos\shapes.png')

#convert to gray
gray_img = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
#blur
blur_img = cv.medianBlur(gray_img , 5)
#canny
canny = cv.Canny(blur_img , 125 , 170)

cv.imshow('canny' , canny)

#detect circles with hough_transform
circles = cv.HoughCircles(canny , cv.HOUGH_GRADIENT , 1 , 100 , param1= 50 , param2= 30 , 
                                minRadius= 0 , maxRadius= 0)

cv.imshow('ci' , circles)

#convert out of circles to int16 data_type
detect_circles = np.uint16(np.around(circles)) 
# print(detect_circles[0])

#loop on circle 
for x,y,r in detect_circles[0 , :] :
    #draw outer circle
    cv.circle(img , (x,y) , r , (0,255,0) , 3)
    #draw circle of radius
    cv.circle(img , (x,y) , 0 , (0,255,0) , 2)

cv.imshow('image' , img)

cv.waitKey(0)
cv.destroyAllWindows()
