"""Image_Processing module."""
import cv2 as cv

"""Numpy module."""
import numpy as np


"""
        ' DOC STRING '
            This code for mouse_events on blank image 
                to draw geometrical shapes

"""


#blank image to draw on it
blank = np.zeros((800,1000,3) , np.uint8)

#show blank image
cv.imshow('image' , blank)

#list for save circle_radius and out point of circle
points_circle = []

#list for save rect_point1 and rect_point2 then draw rect with 2 points
points_rect = []

#list for save line_points but that for 2points only not continuos line As mentioned in task 
points_line = []

def click_events(event , x , y , flags , parameters) :
    '''
        Function that will handle every click event on mouse to do particular something
        
        Left_Double_Click   => Event that will draw circle when make 2 clicks for 2 points center and outpoint

        Right_Double_Click  => Event to Draw rectangle with 2 points means two clicks

        Middle_Double_Click => Event to Draw line with 2 points

        left_Click          => Event to Put text on photo 
    '''    

    #that handle double click on left button mouse
    if event == cv.EVENT_LBUTTONDBLCLK :
        
        #Should add try because if second point of circle will draw circle out of blank image
        try :
            #That condition will draw center point only but other point will draw full circle
            if len(points_circle) == 0  :
                #At first click will draw small circle that represent center 
                cv.circle(blank , (x,y) , 2 , (30,255,255) , 2 )

            #add circle_radius point to list and also out point
            points_circle.append((x,y))

            #check on length list that have 2 points of circle if already == 2 that should draw circle
            if len(points_circle) == 2 :
                #radius = x of point_out - x of point_center 
                radius = points_circle[-1][0] - points_circle[-2][0] 

                #draw circle
                cv.circle(blank , points_circle[-2] , radius , (30,255,255) , -1 )

                #After draw circle must clear list for enter new points for new circles
                points_circle.clear()
        
        #Here will handle error of out circle if raised by draw only small circle
        except :
            cv.circle(blank , (x,y) , 2 , (30,255,255) , 2 )
            #clear list for true points that draw circle
            points_circle.clear()

        #show image blank with circle
        cv.imshow('image' , blank)


    #that handle double click on right button mouse
    if event == cv.EVENT_RBUTTONDBLCLK :

        #That condition will draw first point of rect 
        if len(points_rect) == 0  :
            #At first click will draw small circle that represent point1_rect 
            cv.circle(blank , (x,y) , 2 , (0,255,0) , 1 )

        #add rect_2points to list 
        points_rect.append((x,y))

        #check on length rect_list if == 2 that indicate that second point added  
        if len(points_rect) == 2 :
            #draw rect
            cv.rectangle(blank , points_rect[-2] , points_rect[-1] , (0,255,0) , 4  )

            #After draw rect must clear list for enter new points for new rectangles
            points_rect.clear()

        #show image blank with rect
        cv.imshow('image' , blank)

    #that handle double click on middle button mouse
    if event == cv.EVENT_MBUTTONDBLCLK :

        #That condition will draw first point of rect 
        if len(points_line) == 0  :
            #At first click will draw small circle that represent point1_rect 
            cv.circle(blank , (x,y) , 2 , (255,0,0) , 1 )

        #add line_2points to list 
        points_line.append((x,y))

        #check on length line_list if == 2 that indicate that second point added  
        if len(points_line) == 2 :
            #draw line
            cv.line(blank , points_line[-2] , points_line[-1] , (255,0,0) , 4  )

            #After draw line must clear list for enter new points for new lines
            points_line.clear()

        #show image blank with line
        cv.imshow('image' , blank)     

    #that handle double click on left button mouse
    if event == cv.EVENT_LBUTTONUP :

        #text that will put on blank image
        text = 'Omar Hany Elsayed'

        #When pressed left click mouse once that will put text
        cv.putText(blank , text , (x,y) , cv.FONT_HERSHEY_COMPLEX , 1.0 , (255,0,0) , 3)

        #show image blank with line
        cv.imshow('image' , blank)       

#That function that handle events of mouse
cv.setMouseCallback('image' , click_events )

cv.waitKey(0)
cv.destroyAllWindows()