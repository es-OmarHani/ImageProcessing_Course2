import cv2 as cv
import numpy as np 



#function for method_1
def method_1(frame) :
    '''That method for subtraction_1'''
    #apply subtraction on frame
    frame = fgbg_1.apply(frame)

    #return frame
    return frame 

#function for method_2
def method_2(frame) :
    '''That method for subtraction_2'''
    #apply subtraction on frame
    frame = fgbg_2.apply(frame)

    #return frame
    return frame 


#function for method_3
def method_3(frame) :
    '''That method for subtraction_3'''
    #kernel
    kernel = np.ones((3,3) , np.uint8) 
    #apply subtraction on frame
    frame = fgbg_3.apply(frame)
    #apply opening on it
    frame = cv.morphologyEx(frame , cv.MORPH_OPEN , kernel)

    #return frame
    return frame 

#function for method_4
def method_4(frame) :
    '''That method for subtraction_4'''
    #apply subtraction on frame
    frame = fgbg_4.apply(frame)

    #return frame
    return frame 


#read video
cap = cv.VideoCapture(0)
# r"C:\Users\amora\OneDrive\Documents\Visual Studio Code\Course_Imageproccesing2\videos\vtest.avi.mp4"
#object of method 1
fgbg_1 = cv.bgsegm.createBackgroundSubtractorMOG()

#object of method 2
fgbg_2= cv.createBackgroundSubtractorMOG2()

#object of method 3
fgbg_3 = cv.bgsegm.createBackgroundSubtractorGMG()

#object of method 4
fgbg_4 = cv.createBackgroundSubtractorKNN()

while cap.isOpened() :
    #read frames
    ret , frame = cap.read()

    #make method_1
    frame1 = method_1(frame)
    #show frame from method1
    # cv.imshow('Method_1' , frame1)

    #make method_2
    frame2 = method_2(frame)
    #show frame from method2
    # cv.imshow('Method_2' , frame2)

    #make method_3
    frame3 = method_3(frame)
    #show frame from method3
    # cv.imshow('Method_3' , frame3)

    #make method_4
    frame4 = method_4(frame)
    #show frame from method1
    # cv.imshow('Method_4' , frame4)

    hstack1 = np.hstack((frame1 , frame2))
    hstack2 = np.hstack((frame3 , frame4))
    vstack = np.vstack((hstack1 , hstack2))

    cv.imshow('Methods' , vstack)

    if cv.waitKey(1) & 0xFF == ord('q') :
        break


cv.destroyAllWindows()
cap.release()