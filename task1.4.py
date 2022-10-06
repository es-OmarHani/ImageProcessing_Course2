"""import cv module"""
import cv2 as cv

"""import numpy module"""
import numpy as np

"""
        ' DOC STRING '
            This code for Add Logo on video
"""

#function that rescale frames or images
def scale(image , scale) :
    '''That rescale frames with preferred scale'''
    #get width after scaled it
    width  = int(image.shape[1] * scale)
    #get length after scaled it
    height = int(image.shape[0] * scale)
    #set tuple of width and height that passed to resize function
    dim = (width , height)
    #return resized frame
    return cv.resize(image , dim , interpolation=cv.INTER_AREA)


'''operations on watermark image'''
#read watermark photo
watermark = cv.imread('photos\LOGO.jpg')
#add alpha channel on watermark 
watermark = cv.cvtColor(watermark , cv.COLOR_BGR2BGRA) 
#scale image
watermark = scale(watermark, 0.15)
#watermark_width,height
watermark_height , watermark_width = watermark.shape[:2]

#read video from directory 
cap = cv.VideoCapture("videos\dog.mp4")

#As cap is true path 
while cap.isOpened() :
    #read frame by frame from video
    isTrue , frame = cap.read()
    
    '''operations on video frame'''
    #add alpha channel on frame 
    frame = cv.cvtColor(frame , cv.COLOR_BGR2BGRA) 
    #scale image
    frame = scale(frame, 0.9)
    #frame_width,height
    frame_height , frame_width = frame.shape[:2]

    '''Adding blank image'''
    #create blank with alpha channel
    blank = np.zeros((frame_height , frame_width , 4) , np.uint8)
    #add logo on it
    blank[frame_height - watermark_height : frame_height , frame_width - watermark_width : frame_width] = watermark
    # cv.imshow('blank' , blank)
    # cv.imshow('water' , watermark)
    '''Combine blank image That already have logo with frame '''
    cv.addWeighted(blank , 0.7 , frame , 0.8 , 0 ,frame)

    #show frame after have logo
    cv.imshow('video' , frame)

    #q Key will quit the video
    if cv.waitKey(1) & 0xFF == ord('q') :
        break

cap.release()
cv.destroyAllWindows()

