import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#read image
image = cv.imread(r"C:\Users\amora\OneDrive\Documents\Visual Studio Code\Course_Imageproccesing2\photos\balls2.jfif" , 0)

#convert to threshold image
_ ,image = cv.threshold(image , 220 , 250 , cv.THRESH_BINARY )

#kernel
kernel = np.array((4,4) , np.uint8)

#Dilation
dilate = cv.dilate(image , kernel , iterations=2 )

#Eroding
erode = cv.erode(image , kernel , iterations = 2  )

#opening
opening = cv.morphologyEx(image , cv.MORPH_OPEN , kernel)

#closing
closing = cv.morphologyEx(image , cv.MORPH_CLOSE , kernel)

#gradient
gradient = cv.morphologyEx(image , cv.MORPH_GRADIENT , kernel)


titles = ['original' , 'Dilation' ,'Erode' , 'Opening' , 'Closing' , 'Gradient']
images = [image , dilate , erode , opening , closing , gradient]

for i in range(len(images)) :
    plt.subplot(2 , 3 , i+1 ) #plot multiple images with each other
    plt.imshow(images[i] , cmap='gray' )
    plt.title(titles[i])                #show title of photo
    plt.xticks([]) #show without nums on x_axis 
    plt.yticks([]) #show without nums on y_axis
plt.show()    





