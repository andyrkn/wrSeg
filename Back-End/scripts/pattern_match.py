import cv2 #pip3 install opencv-python
import sys
import os


if __name__ == "__main__":
    large_image = cv2.imread(sys.argv[1])
    cv2.namedWindow('output',cv2.WINDOW_NORMAL)
    cv2.imshow('output',large_image)
    cv2.resizeWindow('output', 1200,600)
    file = open(sys.argv[2] , "r")
    for line in file:
        x_top , y_top , x_bottom , y_bottom  = list(map(int , line.replace("\n" , "").split(" ")))
        print(x_bottom - x_top, y_bottom -y_top)
        cv2.rectangle(large_image, (x_top,y_top),(x_bottom, y_bottom),(0,0,255),2)
        cv2.imshow('output',large_image)
        cv2.waitKey(0)
