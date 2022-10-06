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

_ , th1 = cv.threshold(image , 50 , 255 , cv.THRESH_BINARY)
_ , th2 = cv.threshold(image , 50 , 255 , cv.THRESH_BINARY_INV)
_ , th3 = cv.threshold(image , 115 , 255 , cv.THRESH_TRUNC)
_ , th4 = cv.threshold(image , 115 , 255 , cv.THRESH_TOZERO) 


h1 = np.hstack((th1 , th2))
# cv.imshow("h1" , h1)

h2 = np.hstack((th3 , th4))
# cv.imshow("h2" , h2)


res = np.vstack((h1 , h2))
cv.imshow("Results" , res)

cv.waitKey(0)
cv.destroyAllWindows()