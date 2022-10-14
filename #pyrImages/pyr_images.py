import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#read img
img = cv.imread(r"C:\Users\amora\OneDrive\Documents\Visual Studio Code\Course_Imageproccesing2\photos\Lenna.png")

#gaussian_pyr
img_copy = img.copy()
gaussian_pyr = [img_copy]

for i in range(6) :
    img_copy = cv.pyrDown(img_copy)
    gaussian_pyr.append(img_copy)
    cv.imshow(str(i+1+10) , gaussian_pyr[i])

# laplacian_pyr
img_copy = gaussian_pyr[-1]
laplacian_pyr = [img_copy]
# print(img_copy.shape)
# print()
for i in range(5 , 0 , -1 ):
    #every level get upper of it
    img_extend = cv.pyrUp(gaussian_pyr[i]) 
    # print(img_extend.shape)
    # print(gaussian_pyr[i-1].shape)
    # lap = upper of every level 'Extend' - upper of level 
    laplacian = cv.subtract(gaussian_pyr[i-1] , img_extend )
    laplacian_pyr.append(laplacian)
    #show img
    cv.imshow(str(i) , laplacian)

cv.waitKey(0)
cv.destroyAllWindows()