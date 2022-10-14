import cv2 as cv 
import numpy as np
from matplotlib import pyplot as plt

#read image
image = cv.imread(r"C:\Users\amora\OneDrive\Documents\Visual Studio Code\Course_Imageproccesing2\photos\solt_and_pepper.png")

#kernel
kernel = np.ones((5,5) , np.float32) / 25

#homogenous_filter
homogenous = cv.filter2D(image , -1 , kernel) 

#blur 
blur = cv.blur(image , (5,5))

#gaussian_blur
gaussian = cv.GaussianBlur(image , (3,3) , 0)

#median
median = cv.medianBlur(image , 5)

#bilateral
bilateral = cv.bilateralFilter(image , 9 , 75 , 75)

titles = ['original' , 'homo' ,'blur' , 'gaussian' , 'median' , 'bilateral']
images = [image , homogenous , blur , gaussian , median , bilateral]

for i in range(len(images)) :
    plt.subplot(2 , 3 , i+1 ) #plot multiple images with each other
    plt.imshow(images[i] , cmap='gray' )
    plt.title(titles[i])                #show title of photo
    plt.xticks([]) #show without nums on x_axis 
    plt.yticks([]) #show without nums on y_axis
plt.show()    
