import sys
import cv2

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
