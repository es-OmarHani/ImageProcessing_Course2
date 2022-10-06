import cv2 as cv
import numpy as np

#scaling size
def image_rescale (image , scale) :
    width  = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)
    dim = (width , height)

    return cv.resize(image , dim , interpolation = cv.INTER_AREA)




#read image
image = cv.imread(r'C:\Users\amora\OneDrive\Documents\Visual Studio Code\Course_Imageproccesing2\photos\lady.jpg' , 0)
image = image_rescale(image , 0.6)
# cv.imshow('image' , image)


th1 = cv.adaptiveThreshold(image , 200 , cv.ADAPTIVE_THRESH_MEAN_C , cv.THRESH_BINARY   , 11 , 3)
th2 = cv.adaptiveThreshold(image , 200 , cv.ADAPTIVE_THRESH_GAUSSIAN_C , cv.THRESH_BINARY   , 11 , 3)

res = np.hstack((th1 , th2))
cv.imshow('final' , res)

cv.waitKey(0)
cv.destroyAllWindows()