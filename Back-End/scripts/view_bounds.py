import cv2 #pip3 install opencv-python
import sys
import os


if __name__ == "__main__":
    user_labels = []
    reverse_switcher = {
                "annotation": "0",
                "title": "1",
                "content": "2",
                "footer": "3",
                "pagenumber": "4",
    }
    large_image = cv2.imread(sys.argv[1])
    cv2.namedWindow('output',cv2.WINDOW_NORMAL)
    cv2.imshow('output',large_image)
    cv2.resizeWindow('output', 1200,600)
    file = open(sys.argv[2] , "r")
    with open("test_data.txt", 'r') as fd:
        lines = fd.read().splitlines()
    for line in file:
        x_top , y_top , x_bottom , y_bottom  = list(map(int , line.replace("\n" , "").split(" ")[:4]))
        cv2.rectangle(large_image, (x_top,y_top),(x_bottom, y_bottom),(0,0,255),2)
        cv2.imshow('output',large_image)
        cv2.waitKey(0)
        label = input("Label : ")
        user_labels.append(label)
    with open("train_data.txt" , 'a') as fd:
        for i in range(len(lines)):
                fd.write(lines[i] + " " + reverse_switcher[user_labels[i].strip().replace(" " , "").lower()] + "\n")
