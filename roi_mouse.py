




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