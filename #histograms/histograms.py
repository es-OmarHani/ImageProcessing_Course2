from turtle import color
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#read image
img = cv.imread(r"C:\Users\amora\OneDrive\Documents\Visual Studio Code\Course_Imageproccesing2\photos\group 2.jpg")


#________________________method 1 ______________________________#

plt.hist(img.ravel() , 256 , (0 , 256) )
plt.show()

#________________________method 2 ______________________________#

colors = ['r' , 'g' , 'b']

for i , col in enumerate(colors) :
    hist = cv.calcHist([img] , [i] , None , [256] , [0 , 256])
    #open new figure
    plt.figure()
    #make title for graph
    plt.title('Histograms')
    plt.plot(hist , color = col)
    plt.xlim([0 , 256])

plt.show()