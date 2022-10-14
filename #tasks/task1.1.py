"""Image_Processing module."""
import cv2 as cv

"""
        ' DOC STRING '
            This code for controlling Live videos
                    by [making grey scale on video or colorful video ,
                        save image from video or  save video  ,
                        pause or continue video ]
"""

#make capture that read video from web camera (live video)
cap = cv.VideoCapture(0)

#make status that will initialized by none but in every pressed on keyboard will change according to key
status = 'None'

#counter to pass it for name of saved_image
counter = 0

# Define the codec and create VideoWriter object
four_cc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('video.avi',four_cc, 20.0, (640,480))

#loop on capture video frame by frame to show them on screen
while cap.isOpened() :
    #That will return every true frame from video to show it
    ret , frame = cap.read()

    if ret == True : # AS frames is reading true will execute the code
        if status == 'None' : #As there is no key pressed will show original frames
            cv.imshow('video' , frame)

        #key that will used for handling when user pressed key on keyboard
        key = cv.waitKey(1)

        if key & 0xFF == ord('g') or status == 'Grey' or  status == 'Grey' :
            #G key will covert frame to grey scale
            frame = cv.cvtColor(frame , cv.COLOR_BGR2GRAY)
            cv.imshow('video' , frame)
            status = 'Grey'

        if key & 0xFF == ord('c') or status == 'Colorful':
            #C key will covert frame to colorful frame if it isn't on color frame
            cv.imshow('video' , frame)
            status = 'Colorful'

        if key & 0xFF == ord('s') :
            #S key will save current frame
            counter += 1
            image = f'Image_{counter}.png' #var to take a new name every time if s key is pressed
            cv.imwrite( image , frame)


        if key & 0xFF == ord('f') or status == 'Flip' :
            #F key will flip the frame
            #2nd parameter is be // 0 for flip over x_axis // 1 for flip over y_axis // -1 for flip in both axis
            frame = cv.flip(frame , 0)
            cv.imshow('video' , frame)
            status = 'Flip'


        if key & 0xFF == ord('m') or status == 'Record_Start' :
            #m key will start write frame by frame in video
            out.write(frame)
            status == 'Record_Start'

        if key & 0xFF == ord('n')  :
            #n key will release out from write frames
            out.release()


        if key & 0xFF == ord('p') :
            #P key will pause the video
            cv.waitKey()  #by using cv.waitkey without any int number will freeze the frame

        if key & 0xFF == ord('o') :
            cv.waitKey(0) #by using cv.waitkey with 0 only will continue capturing frames again

        if key & 0xFF == ord('q') :
            #Q key will quit the video by breaking loop
            break

    else : # If frame not true will break loop
        break

out.release()
cap.release()
cv.destroyAllWindows()

