import cv2
import cv2 as cv
import numpy as np
import math

img = cv2.imread('C:/Users/bryan/Desktop/OpenCV Workshop - distro 5c/OpenCV Workshop/tek1.png')
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret,thresh = cv.threshold(imgray ,0,255,0)
contours,hierarchy = cv.findContours(
    thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cnt = contours[23]

hull = cv.convexHull(cnt)

M = cv.moments(cnt)
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

cv.circle(img, (cx,cy), 3, (0, 255, 255),5 )

cv.drawContours(img, [hull], 0, (255,255,0), 3)

cv.imshow('opdracht3b',img)

k = cv.waitKey(0)
cv.destroyAllWindows()