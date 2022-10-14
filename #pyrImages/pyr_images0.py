import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#read img
img = cv.imread(r'C:\Users\amora\OneDrive\Documents\Visual Studio Code\Course_Imageproccesing2\photos\Lenna.png')

layer= img.copy()
gp = [layer]

for i in range(6) :
    layer = cv.pyrDown(layer)
    gp.append(layer)

layer = gp[-1]
lp=[layer]

for i in range(5,0,-1) :
    gauss_extend = cv.pyrUp(gp[i])
    lap = cv.subtract(gp[i-1] , gauss_extend)
    cv.imshow(str(i) , lap )

cv.waitKey(0)
cv.destroyAllWindows()    
