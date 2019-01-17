"""
User Guide

Run collect-data from terminal , each square box will be drawn individually, then you need to press a key ,
then write the corresponding label in the terminal , rinse and repeat
"""
import cv2 #pip3 install opencv-python
import sys
import os

def write_data(binary, path):
    shape = cv2.imread(binary).shape[:2][::-1]
    with open(path , "r") as file_input , open("test_data.txt" , "w") as file_output:
        input_data = []
        for line in file_input:
            data = []
            data = line.replace("\n" , " ").split()
            features = list(map(float ,data))
            features[2] -= features[0] # get width
            features[3] -= features[1] # get height
            features = [features[i] / shape[i % 2] for i in range(len(features))] # Normalize
            input_data.append(features)
        for line in input_data:
            for i in range(len(line) - 1):
                file_output.write(str(line[i]) + " ")
            file_output.write(str(line[len(line) - 1]) + "\n")

if __name__ == "__main__":
    write_data(sys.argv[1],sys.argv[2])
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
