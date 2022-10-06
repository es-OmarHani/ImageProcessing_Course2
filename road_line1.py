import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#function that get roi
def ROI_func(image , vertices) :
    #get mask image with blank all data as original
    mask = np.zeros_like(image)
    #get color channels
    channel_counter = image.shape[2]
    #mask_color_channel
    mask_color_channel = (255,) * channel_counter
    #fill blank in ROI region with only colors
    im = cv.fillPoly(mask , vertices , mask_color_channel)
    # cv.imshow('im' , im)
    #now mask fill with original image
    masked_img = cv.bitwise_and(img , mask)

    return masked_img 

#read image
img = cv.imread(r'C:\Users\amora\OneDrive\Documents\Visual Studio Code\Course_Imageproccesing2\photos\road1.jpg')

width  = img.shape[1] 
height = img.shape[0]

#roi_vertices
ROI_vertices = [
    (0,200),
    (width/2 , 15),
    (width , 200)
]

#now pass image to function
cropped_img =  ROI_func(img , np.array( [ROI_vertices] , np.int32))

#show image
cv.imshow('image' , cropped_img)

cv.waitKey(0)
cv.destroyAllWindows()