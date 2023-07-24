import numpy as np
import cv2 as cv
import math


img = cv.imread('C:/Users/bryan/Desktop/OpenCV Workshop - distro 5c/OpenCV Workshop/bouten_moeren1.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
grayBlur = cv.GaussianBlur(gray, (25,25), 0)
ret,threshbinary = cv.threshold(grayBlur, 180, 255,cv.THRESH_BINARY_INV)


contours, hierarchy = cv.findContours(
    threshbinary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

hierarchy = hierarchy[0]
for cnr in range(len(contours)):
    cnt = contours[cnr]
    area = cv.contourArea(cnt)
    perimeter = cv.arcLength(cnt, True)
    factor = 4 * math.pi * area / perimeter**2
    holes = 0.00
    child = hierarchy[cnr][2]

    if factor < 0.50:
        cv.drawContours(img, [cnt], 0, (0, 255, 255),3)
    elif factor < 0.80:
        cv.drawContours(img, [cnt], 0, (0, 0, 225),3)
    elif (factor > 0.8) & (area > 500):
        cv.drawContours(img, [cnt], 0, (0, 255, 0), )

    while child >= 0:
        holes += cv.contourArea(contours[child])
        child = hierarchy[child][0]
        cv.drawContours(img, [cnt], 0, (255, 0, 0), 3)
    print(area, factor, holes)

cv.imshow('img',img)

q = cv.waitKey(0)
print(q)
cv.destroyAllWindows()