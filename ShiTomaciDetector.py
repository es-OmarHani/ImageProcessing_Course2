import cv2 as cv
import numpy as np



#rescale img
def rescale_size(image , scale ) :
    width  = image.shape[1] * scale 
    height = image.shape[0] * scale
    dim = (width , height)

    return cv.resize(image , dim , interpolation = cv.INTER_AREA  )

#read image
img = cv.imread(r'C:\Users\amora\OneDrive\Documents\Visual Studio Code\Course_Imageproccesing2\photos\PointDetection.jpg')
# img = rescale_size(img , 0.8)

#convert to gray
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

#make image with float32
# gray = np.float32(gray)

#get corners
corners = cv.goodFeaturesToTrack(gray , 100 , 0.01 , 10)
corners = np.int0(corners)

#loop on corners
for i in corners :
    x , y = i.ravel() 
    cv.circle(img , (x,y) , 1 , [0,0,255] , 2)


cv.imshow('image' , img)
cv.waitKey(0)
cv.destroyAllWindows()