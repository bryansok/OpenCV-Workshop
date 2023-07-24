import math
import numpy
import numpy as np
import cv2

## opdracht 1
def opdracht1():
    img = cv2.imread('C:/Users/bryan/Desktop/OpenCV Workshop - distro 5c/OpenCV Workshop/tek1.png')
    cv2.imshow('logo',img)
    k = cv2.waitKey(0)
    print(k)
    cv2.destroyAllWindows()

opdracht1()