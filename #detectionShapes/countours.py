import cv2 as cv
import numpy as np


#read image
img = cv.imread(r'C:\Users\amora\OneDrive\Documents\Visual Studio Code\Course_Imageproccesing2\photos\opencv-4.1-feature-image.png' , 0)



#____________________________________________code 1___________________________________#

blur = cv.GaussianBlur(img , (5,5) , 0)

#get thrash with track bar
_ , thresh = cv.threshold(blur , 180 , 255 , cv.THRESH_BINARY )

#get counters
contours1 , _ = cv.findContours(thresh , cv.RETR_TREE , cv.CHAIN_APPROX_SIMPLE )

#draw contours
final_img1 = cv.drawContours(img , contours1 , -1 , (0,255,0) , 3 , cv.FONT_HERSHEY_SCRIPT_SIMPLEX)

cv.imshow('image1' , final_img1 )

print(f'number of contours = {len(contours1)}')


#____________________________________________code 2___________________________________#

canny = cv.Canny(img , 170 , 170 )

#get counters
contours2 , _ = cv.findContours(canny , cv.RETR_TREE , cv.CHAIN_APPROX_SIMPLE )

#draw contours
final_img2 = cv.drawContours(img , contours2 , -1 , (0,255,0) , 3 , cv.FONT_HERSHEY_SCRIPT_SIMPLEX)

cv.imshow('image2' , final_img2 )

print(f'number of contours = {len(contours2)}')

cv.waitKey(0)
cv.destroyAllWindows()