import cv2
import cv2 as cv
import numpy as np
import math

img = cv2.imread('C:/Users/bryan/Desktop/OpenCV Workshop - distro 5c/OpenCV Workshop/tek2.png')
while(1):
    # Convert BGR to HSV
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    
    # define range of color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    
    lower_green = np.array([50,50,50])
    upper_green = np.array([70,255,255])
    
    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])
    rmask1 = cv.inRange(hsv, lower_red, upper_red)
    lower_red = np.array([170,50,50])
    upper_red = np.array([180,255,255])
    rmask2 = cv.inRange(hsv, lower_red, upper_red)

    mask1 = cv.inRange(hsv, lower_blue, upper_blue)
    mask2 = cv.inRange(hsv, lower_green, upper_green)
    #mask3 = cv.inRange(hsv, lower_red, upper_red)
    mask3 = rmask1 | rmask2
    
    # Bitwise-AND mask and original image
    img1 = cv.bitwise_and(img,img, mask=mask1)
    img2 = cv.bitwise_and(img,img, mask=mask2)
    img3 = cv.bitwise_and(img,img, mask=mask3)
    
    cv.imshow('img',img)
    cv.imshow('img1',img1)
    cv.imshow('img2',img2)
    cv.imshow('img3',img3)
    cv.imshow('mask1',mask1)
    cv.imshow('mask2',mask2)
    cv.imshow('mask3', mask3)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()