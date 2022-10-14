import cv2 as cv 
import numpy as np
from matplotlib import pyplot as plt

#read image
image = cv.imread(r"C:\Users\amora\OneDrive\Documents\Visual Studio Code\Course_Imageproccesing2\photos\messi.jpeg" , 0)

#laplacian
lab = cv.Laplacian(image , cv.CV_64F , ksize= 5)
lap = np.uint8(np.absolute(lab))

#sobel_x & sobel_y
sobel_x = cv.Sobel(image , cv.CV_64F , 1 , 0)
sobel_y = cv.Sobel(image , cv.CV_64F , 0 , 1) 

res_sobel = cv.bitwise_or(sobel_x , sobel_y)

titles = ['original' , 'lab' ,'sobel_x' , 'sobel_y' , 'final' ]
images = [image , lab , sobel_x , sobel_y , res_sobel]


for i in range(len(images)) :
    plt.subplot(2 , 3 , i+1 ) #plot multiple images with each other
    plt.imshow(images[i] , cmap='gray' )
    plt.title(titles[i])                #show title of photo
    plt.xticks([]) #show without nums on x_axis 
    plt.yticks([]) #show without nums on y_axis
plt.show()   



#canny
def track_bar (x) :
    pass

#crate track_bar
cv.namedWindow('canny')
cv.createTrackbar('L_value' , 'canny' , 0 , 255 , track_bar)
cv.createTrackbar('H_value' , 'canny' , 0 , 255 , track_bar)


while True :
    
    #read image
    image = cv.imread(r"C:\Users\amora\OneDrive\Documents\Visual Studio Code\Course_Imageproccesing2\photos\cats.jpg" , 0)

    L_value = cv.getTrackbarPos('L_value' , 'canny')
    H_value = cv.getTrackbarPos('H_value' , 'canny')

    canny = cv.Canny(image , L_value , H_value)

    cv.imshow('canny_1' , canny)

    if cv.waitKey(0) & 0xFF == ord('q') :
        break

cv.waitKey(0)
cv.destroyAllWindows()    

