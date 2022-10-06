import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#_______________________________________Method 1__________________________________________#

#read img1
img_1 = cv.imread(r'C:\Users\amora\OneDrive\Documents\Visual Studio Code\Course_Imageproccesing2\photos\orange.jpg')

#read img2
img_2 = cv.imread(r'C:\Users\amora\OneDrive\Documents\Visual Studio Code\Course_Imageproccesing2\photos\apple.jpg')

#image
img_3 = cv.imread(r"C:\Users\amora\OneDrive\Documents\Visual Studio Code\Course_Imageproccesing2\photos\Lenna.png")

#rescale 2 images on the same of image 2
def rescale_size(image , scale = 1) :
    width  = img_3.shape[1] * scale 
    height = img_3.shape[0] * scale
    dim = (width , height)

    return cv.resize(image , dim , interpolation = cv.INTER_AREA )


#rescale 2 images with size of smaller
img_1_original = rescale_size(img_1)
img_1 = img_1_original.copy()

img_2_original = rescale_size(img_2)
img_2 = img_2_original.copy()

print(img_1.shape)
print(img_2.shape)

#_______________________________________Method 2__________________________________________#
#gaussian of img_1
gauss_img1 = [img_1]

for i in range(6) :
    img_1 = cv.pyrDown(img_1)
    gauss_img1.append(img_1)

#gaussian of img_2
gauss_img2 = [img_2]

for i in range(6) :
    img_2 = cv.pyrDown(img_2)
    gauss_img2.append(img_2)    


#_______________________________________Method 3__________________________________________#

#laplacian of img_1
img_1 = gauss_img1[5]
laplacian_img1 = [img_1]
# print(img_1.shape)

for i in range(5,0,-1) :
    img1_extend = cv.pyrUp(gauss_img1[i])
    print(img1_extend.shape)
    print(gauss_img1[i-1].shape)
    laplacian = cv.subtract(gauss_img1[i-1] , img1_extend)
    laplacian_img1.append(laplacian)

#laplacian of img_2
img_2 = gauss_img2[5]
laplacian_img2 = [img_2]

for i in range(5,0,-1) :
    img2_extend = cv.pyrUp(gauss_img2[i])
    laplacian = cv.subtract(gauss_img2[i-1] , img2_extend)
    laplacian_img2.append(laplacian)


#_______________________________________Method 4__________________________________________#

#make mix 2 [left of img1 with right of img 2] images in laplacian

img1_img2_pyr = []

for img1_lap , img2_lap in zip(laplacian_img1 , laplacian_img2) :
    #read columns
    cols = img_1.shape[1]
    #mix images
    laplacian = np.hstack((img2_lap[ : , 0 : int(cols/2) ] , img1_lap[ : , int(cols/2) : ]))
    #append laplacian to list
    img1_img2_pyr.append(laplacian)

#_______________________________________Method 5__________________________________________#

#re_construction image

img1_img2_reconstruct = img1_img2_pyr[0]

for i in range(1 , 6) : 
    img1_img2_reconstruct = cv.pyrUp(img1_img2_reconstruct)
    img1_img2_reconstruct = cv.add(img1_img2_pyr[i] , img1_img2_reconstruct)

img_stack = np.hstack((img_1_original[ : , : int(cols/2) ] , img_2_original[ : , int(cols/2) : ]))

cv.imshow('img_1' , img_1_original)
cv.imshow('img_2' , img_2_original)
cv.imshow('000' , img_stack )
cv.imshow('img1 with img2' , img1_img2_reconstruct)

cv.waitKey(0)
cv.destroyAllWindows()

