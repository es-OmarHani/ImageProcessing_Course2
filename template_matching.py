import cv2 as cv
import numpy as np

#read image original 
img_original_1 = cv.imread(r'C:\Users\amora\OneDrive\Documents\Visual Studio Code\Course_Imageproccesing2\photos\messi.jpeg' )
img_original = cv.cvtColor(img_original_1 , cv.COLOR_BGR2GRAY)

#read template img
img_template = cv.imread(r'C:\Users\amora\OneDrive\Documents\Visual Studio Code\Course_Imageproccesing2\photos\messi2.jpeg' , 0 )

width_temp  = img_template.shape[1]
height_temp = img_template.shape[0]


#result of temp match
result = cv.matchTemplate(img_original , img_template , cv.TM_CCOEFF_NORMED)

# print(result)

#getting brightness point
threshold = 0.9995
location = np.where(result >= threshold )

# print(location)

#make rect on point
for point in zip(*location[::-1]) :

    #making rect
    cv.rectangle(img_original_1 , point , (point[0]+width_temp , point[1]+height_temp) , (0,255,0) , 1 )


#show image
cv.imshow('image' , img_original_1)

cv.waitKey(0)
cv.destroyAllWindows()