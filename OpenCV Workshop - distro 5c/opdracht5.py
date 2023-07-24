import numpy as np
import cv2 as cv
import math

img = cv.imread('C:/Users/bryan/Desktop/OpenCV Workshop - distro 5c/OpenCV Workshop/dobbelstenen.png')
gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

ret, threshold = cv.threshold(gray, 10, 255, cv.THRESH_BINARY)
contours, hierarchy = cv.findContours(
    threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
dice = []

for cnr in range(len(contours)):
    x, y, w, h = cv.boundingRect(contours[cnr])

    die = gray[y:y+h, x:x+w]
    dieholes = 0
    ret, thresh = cv.threshold(die, 200, 255, cv.THRESH_BINARY)
    
    cont, hier = cv.findContours(
        thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    for eyes in range(len(cont)):
        cnt = cont[eyes]
        area = cv.contourArea(cnt)
        perimeter = cv.arcLength(cnt, True)
        if perimeter != 0:
            if (area > 100) & ((4 * math.pi * area / perimeter**2) > 0.80):
                dieholes += 1

    cv.drawContours(die, cont, -1, (0,0,0), 3)
    cv.imshow("die" + str(x), die)
    
    dice.append(dieholes)

dice.sort()
print(dice)

q = cv.waitKey(0)
cv.destroyAllWindows()