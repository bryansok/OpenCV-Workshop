import cv2 as cv
import numpy as np
import math

def opdracht4a():
    img = cv.imread('C:/Users/bryan/Desktop/OpenCV Workshop - distro 5c/OpenCV Workshop/bouten_moeren1.jpg')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    grayBlur = cv.GaussianBlur(gray, (25,25), 0)
    ret, th = cv.threshold(grayBlur, 180, 255, cv.THRESH_BINARY_INV)
    
    contours, hierarchy = cv.findContours(th, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        area = cv.contourArea(cnt)
        # teken alleen contouren met een oppervlakte groter dan 100
        if area > 100:
            cv.drawContours(img, [cnt], -1, (0,255,255), 3)
            
    cv.imshow('img',img)
    q = cv.waitKey(0)
    print(q)
    cv.destroyAllWindows()   
       
opdracht4a()