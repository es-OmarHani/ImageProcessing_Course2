"""Image_Processing module."""
import cv2 as cv

"""Numpy module."""
import numpy as np

'''date_time module.'''
import datetime


"""
        ' DOC STRING '
            This code for mouse_events on videos like select ROI , 
            apply filters on video with its color channels as red , blue , green 
            but all of this with mouse click events 

"""

#First , set the variable which capture video 
cap = cv.VideoCapture(0)

#list for points of ROI when deal with it by mouse events
points_roi = []

global counter 
counter = 'zero'

"""
                    Status 
    it indicate which region you in at this time in video 
    OR with another discussion that should apply to apply the selected filter every time frame is captured 
"""
status = 'None'



def click_event (event , x , y , flags , parameters) :
    '''
        That function handles all events by click mouse 
        
        Left_Double_Click  => Event that select ROI by select 4 points that border object in photo
                            Then apply it on top left corner

        Right_Click        => Event to show blue channel of selected frame or image 

        Right_Double_Click => Event to show green channel of selected frame or image 

        Middle_Click       => Event to show red channel of selected frame or image 
    '''

    #That Event handle ROI selection
    if event == cv.EVENT_LBUTTONDBLCLK :
        '''Note : That method also used for wrap respective / Bird view 
                Image border should taken by following these steps :
                        1.Top left corner
                        2.Top right corner
                        3.bottom left corner
                        4.bottom right corner 
        '''

        #Adding selected point by mouse Left_double_click to list  
        points_roi.append((x,y))

        #Draw circle on place of click to indicate for user the selected point
        cv.circle(frame , (x,y) , 5 , (0,0,255) , -1)

        # #That handle when list has 4 points that means that user selected border of object in frame or image
        # if len(points_roi) == 4 :
            
        #     #That indicate width , height of output ROI
        #     width  = points_roi[1][0] - points_roi[0][0]
        #     height = points_roi[2][1] - points_roi[0][1]

        #     #matrix_1 For selected points border object
        #     matrix_1 = np.float32([ points_roi[0] , points_roi[1] , points_roi[2] , points_roi[3]  ])
            
        #     #matrix_2 For output image border
        #     matrix_2 = np.float32([ (0,0) , (width,0) , (0,height) , (width , height)  ])

        #     #matrix final that get respective view from selected points
        #     matrix_final = cv.getPerspectiveTransform(matrix_1 , matrix_2)

        #     #output from matrix_final will be ROI 
        #     roi_img = cv.warpPerspective(frame , matrix_final , (width , height))

        #     #Here that will put selected ROI on top corner of image or frame
        #     frame [0 : height  , 0 : width ] = roi_img

        #     #After all of that clear list to can add new points to select new ROI
        #     points_roi.clear()

        #     #That for show selected ROI from frame or image
        #     cv.imshow('cropped' , roi_img)

        # #That for show frame
        # cv.imshow('image' , frame )    

    #That Event get new_frame with blue filter of original frame
    if event == cv.EVENT_RBUTTONUP :
        
        #By splitting image will get 3 channels
        b , g , r = cv.split(frame)
        #Adding or merge blue chancel to make out image with 3 channels not 1 chanel
        blue = cv.merge([b , blank , blank])
        #Show blue channel
        cv.imshow('image_blue' , blue) 

    #That Event get new_frame with green filter of original frame
    if event == cv.EVENT_RBUTTONDBLCLK :

        #By splitting image will get 3 channels
        b , g , r = cv.split(frame)
        #Adding or merge green chancel to make out image with 3 channels not 1 chanel
        green = cv.merge([blank , g , blank])
        #Show green channel
        cv.imshow('image_green' , green)



    if event == cv.EVENT_MBUTTONUP :

        #By splitting image will get 3 channels
        b , g , r = cv.split(frame)
        #Adding or merge red chancel to make out image with 3 channels not 1 chanel
        red = cv.merge([blank , blank , r])
        #Show red channel
        cv.imshow('image_red' , red) 

#As capture is true opened which means path of video is true or selection camera is available 
while cap.isOpened() :
    #That will return every true frame from video to show it
    ret , frame = cap.read()
    #That will make balnk image which used to merged with channels in mouse_events
    blank = np.zeros((frame.shape[:2]) , np.uint8)

    if ret == True : #If frames is True will do our Code
        
        #Var that save time only
        time = f"Time : {datetime.datetime.now().time()}"
        #var that save date
        date = f"Date : {datetime.datetime.now().date()}"
        #var that save two variables
        date_time = f"\t{date} \t {time}".expandtabs(2)
        #position will show text
        position = (0 , 20) 
        #Function that put text on image or frame
        cv.putText(frame , str(date_time) , position , cv.FONT_HERSHEY_COMPLEX_SMALL , 1.0 , (0,255,0) , 1 )        
        
        #As status is None that means there is no selection for any filter so show original image
        if status == 'None' :
            cv.imshow('image' , frame)

        # That key is anding with keyboard key to detect which key is pressed
        key = cv.waitKey(1)

        #When key a is pressed will return original filter of video if already selected filter on it
        if key & 0xFF == ord('a') or status == 'Normal' :

            #That show frame
            cv.imshow('image' , frame)
            #That only flag to know last state every loop if no selected filter 
            status = 'Normal'

        #when key b is pressed will make blue filter on frame which is blue channel of frame
        if key & 0xFF == ord('b') or status == 'blue' :
            #By splitting image will get 3 channels
            b , g , r = cv.split(frame)
            #Adding or merge blue chancel to make out image with 3 channels not 1 chanel
            blue = cv.merge([b , blank , blank])
            #show image_filtered on the same frame
            cv.imshow('image' , blue) 
            #That only flag to know last state every loop if no selected filter 
            status = 'blue'
            
        #when key g is pressed will make green filter on frame which is blue channel of frame
        if key & 0xFF == ord('g') or status == 'green' :
            #By splitting image will get 3 channels
            b , g , r = cv.split(frame)
            #Adding or merge green chancel to make out image with 3 channels not 1 chanel
            green = cv.merge([blank , g , blank])
            #show image_filtered on the same frame
            cv.imshow('image' , green) 
            #That only flag to know last state every loop if no selected filter 
            status = 'green'        

        #when key r is pressed will make red filter on frame which is blue channel of frame
        if key & 0xFF == ord('r') or status == 'red' :
            #By splitting image will get 3 channels
            b , g , r = cv.split(frame)
            #Adding or merge red chancel to make out image with 3 channels not 1 chanel
            red = cv.merge([blank , blank , r])
            #show image_filtered on the same frame
            cv.imshow('image' , red) 
            #That only flag to know last state every loop if no selected filter 
            status = 'red'    
            
        #if q key is pressed will exit from video
        if key & 0xFF == ord('q') :
            break 

 #That handle when list has 4 points that means that user selected border of object in frame or image
        if len(points_roi) == 4 :
            
            #That indicate width , height of output ROI
            width  = points_roi[1][0] - points_roi[0][0]
            height = points_roi[2][1] - points_roi[0][1]

            #matrix_1 For selected points border object
            matrix_1 = np.float32([ points_roi[0] , points_roi[1] , points_roi[2] , points_roi[3]  ])
            
            #matrix_2 For output image border
            matrix_2 = np.float32([ (0,0) , (width,0) , (0,height) , (width , height)  ])

            #matrix final that get respective view from selected points
            matrix_final = cv.getPerspectiveTransform(matrix_1 , matrix_2)

            #output from matrix_final will be ROI 
            roi_img = cv.warpPerspective(frame , matrix_final , (width , height))

            #Here that will put selected ROI on top corner of image or frame
            frame [0 : height  , 0 : width ] = roi_img

            #After all of that clear list to can add new points to select new ROI
            points_roi.clear()

            #That for show selected ROI from frame or image
            cv.imshow('cropped' , roi_img)

            #That for show frame
            cv.imshow('image' , frame )    

        #That function that handle events of mouse
        cv.setMouseCallback('image' , click_event)

    else : #If any frame is false will break loop 
        break

cv.waitKey(0)
cv.destroyAllWindows()
