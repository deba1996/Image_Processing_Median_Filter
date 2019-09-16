import numpy as np
import cv2

img = cv2.imread("Image 6.JPG")#read the image

cv2.namedWindow('Unfiltered Image', cv2.WINDOW_NORMAL)#name the window
cv2.imshow('Unfiltered Image',img)#show the unfiltered image
cv2.waitKey(0)
print "Processing..."

# median filter - takes median from group of pixels
# mostly depends on kernel size
# median for sorted vector [1 1 2 2 2 3 4 5 5] is 2

# OpenCV median = cv2.medianBlur(src, ksize[, dst])

myIMG = cv2.medianBlur(img,3)#apply filter

cv2.namedWindow('Processed Image', cv2.WINDOW_NORMAL)#name the window
cv2.imshow('Processed Image', myIMG)#show the filtered image
cv2.waitKey(0)
print "Done!"
