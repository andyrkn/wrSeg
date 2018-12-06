import sys
from classify import minDist
import cv2


def write_data(binary, path):
    shape = cv2.imread(binary).shape[:2]
    with open(path , "r") as file_input , open("train_data.txt" , "a") as file_output:
        input_data = []
        for line in file_input:
            data = []
            data = line.replace("\n" , " ").split()
            path = data[0:1]
            features = list(map(int ,data[1:]))
            features = [features[i] / shape[i % 2] for i in range(len(features))] # Normalize
            input_data.append(path + features)
        for line in input_data:
            for elem in line:
                file_output.write(str(elem) + " ")
            file_output.write(str(minDist(line , input_data)) + "\n")

if __name__ == "__main__":
    write_data(sys.argv[1],sys.argv[2])
