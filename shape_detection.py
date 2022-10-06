import cv2 as cv
import numpy as np

#read image
img = cv.imread(r"C:\Users\amora\OneDrive\Documents\Visual Studio Code\Course_Imageproccesing2\photos\shapes.png")

#rescale image
def rescale_size(image , scale ) :
    width  = int(img.shape[1] * scale )
    height = int(img.shape[0] * scale)
    dim = (width , height)

    return cv.resize(image , dim , interpolation = cv.INTER_AREA )

#rescale
img = rescale_size(img , 0.6)

#gray img
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

#thresh
_ , thresh = cv.threshold(gray , 240 , 255 , cv.THRESH_BINARY)

#canny
canny = cv.Canny(thresh , 240 , 255)

#contours
contours , _ = cv.findContours(canny, cv.RETR_TREE , cv.CHAIN_APPROX_SIMPLE)

print(f'contours = {len(contours)}')

for contour in contours :
    #approximation contours
    approx = cv.approxPolyDP(contour , 0.01*cv.arcLength(contour , True) , True )

    #bounding rect
    x_bound , y_bound , w ,h = cv.boundingRect(contour)

    #get x & y 
    x = approx.ravel()[0]
    y = approx.ravel()[1] + 50

    if cv.contourArea(contour) < 6000 :
        continue

    #draw contour
    cv.drawContours(img , [approx] , 0 , (0,0,0) , 2)

    #get shapes
    if len(approx) == 3 :
        #triangle
        cv.putText(img , 'Triangle' , (x,y) , cv.FONT_HERSHEY_COMPLEX_SMALL , 1 , 0 )

    if len(approx) == 4 :
        #get ratio between w/h
        ratio = float(w)/h
        print(ratio)

        if ratio >= 0.98 and ratio <= 1.03 :
            #square
            cv.putText(img , 'Square' , (x,y) , cv.FONT_HERSHEY_COMPLEX , 1 , 0 )

        else :
            #rect
            cv.putText(img , 'Rectangle' , (x,y) , cv.FONT_HERSHEY_COMPLEX_SMALL , 1 , 0 )   

    if len(approx) == 5 : 
        cv.putText(img , 'Pentagon' , (x,y) , cv.FONT_HERSHEY_COMPLEX_SMALL , 1 , 0 )   

    if len(approx) == 6 : 
        cv.putText(img , 'Hexagonal' , (x,y) , cv.FONT_HERSHEY_COMPLEX_SMALL , 1 , 0 ) 

    if len(approx) == 10 : 
        cv.putText(img , 'Star' , (x,y) , cv.FONT_HERSHEY_COMPLEX_SMALL , 1 , 0 )  

    else :
        cv.putText(img , 'circle' , (x,y) , cv.FONT_HERSHEY_COMPLEX_SMALL , 1 , 0 )    


#show image
cv.imshow('image' , img)

cv.waitKey(0)
cv.destroyAllWindows()