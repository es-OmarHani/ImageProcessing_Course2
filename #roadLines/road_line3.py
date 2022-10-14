import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


#read image
img = cv.imread(r'C:\Users\amora\OneDrive\Documents\Visual Studio Code\Course_Imageproccesing2\photos\road1.jpg')


#function that get roi
def ROI_func(image , vertices) :
    #get mask image with blank all data as original
    mask = np.zeros_like(image)
    #get color channels
    # channel_counter = image.shape[2]
    #mask_color_channel
    mask_color_channel = 255
    #fill blank in ROI region with only colors
    im = cv.fillPoly(mask , vertices , mask_color_channel)
    #now mask fill with original image
    masked_img = cv.bitwise_and(image , mask)

    return masked_img


#function that draw lines of ROI Edges to original
def Draw_lines(image , lines) :
    #make blank image
    img_blank = np.zeros((image.shape[0] , image.shape[1] , 3) , np.uint8)
    #loop through hough_linesp to get points of lines
    for line in lines :
        #get 2points of line
        x1 , y1 ,x2 , y2 = line[0]
        #draw line on blank image
        cv.line(img_blank , (x1,y1) , (x2,y2) , (0,255,0) , 1 )

    #now merge 2 photos with each other
    img_merged = cv.addWeighted(image , 0.8 , img_blank , 1.0 , 0 )    

    return img_merged

#function that do all process
def Process_road_detect(img) :
    
    #get width , height of image
    width  = img.shape[1] 
    height = img.shape[0]

    #roi_vertices
    ROI_vertices = [
        (0,height),
        (0,200),
        (width/2 , 15),
        (width , 200),
        (width , height)
    ]

    #gray image
    img_gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
    #canny img
    img_canny = cv.Canny(img_gray , 100 , 150 )

    #now pass image to function but now get ROI from canny image
    cropped_img =  ROI_func(img_canny , np.array( [ROI_vertices] , np.int32))

    #now get lines form hough_Lines
    lines = cv.HoughLinesP(cropped_img , 1 , np.pi/180 , 100 , minLineLength=100 , maxLineGap=10 )

    #now pass lines with cropped image to draw function
    img_merged = Draw_lines(img , lines)

    return img_merged


#read video
cap = cv.VideoCapture(r'C:\Users\amora\OneDrive\Documents\Visual Studio Code\Course_Imageproccesing2\videos\lanes_clip.mp4')

while cap.isOpened() :
    #read frame
    ret , frame = cap.read()

    #pass frame to process function
    frame = Process_road_detect(frame)

    #show frame
    cv.imshow('Road' , frame)

    #break video
    if cv.waitKey(1) & 0xFF == ord('q') :
        break

cv.destroyAllWindows()
cap.release()    


