import os
import sys
import re
import subprocess
import json

print(os.getcwd())
print(sys.argv)

ADDNOTATION = "Adnotation"
TITLE = "Title"
CONTENT = "Content"
FOOTER = "Footer"
PAGE_NR = "PageNumber"

filename = sys.argv[1].split('.')[-2]
extension = sys.argv[1].split('.')[-1]
# print(sys.argv[1].split('.'))
# f = open('./../processed-images/' + filename + '.json', 'w')
# f.write("{}\n")
# f.close()

try:
    res = subprocess.call('./bash-script ./../assets/' + filename + '.' + extension, shell=True)  # + ' -o' + ' temp')
    print("\n\n\nHELLLLLLLLLLLO\n\n\n")
except Exception as e:
    print(e)

coordinates_file = open('column_indexes.txt', 'r')
coordinates_line = coordinates_file.readlines()
coordinates_file.close()
data = dict()
data[TITLE] = []
data[CONTENT] = []
data[ADDNOTATION] = []
data[FOOTER] = []
data[PAGE_NR] = []
data_type = 0
for coordinates in coordinates_line:
    coordinates = coordinates.strip('\n').split(' ')

    if coordinates[4] == TITLE:
        data[TITLE].append([int(coordinates[0]), int(coordinates[1]), int(coordinates[2]), int(coordinates[3])])
    elif coordinates[4] == CONTENT:
        data[CONTENT].append([int(coordinates[0]), int(coordinates[1]), int(coordinates[2]), int(coordinates[3])])
    elif coordinates[4] == ADDNOTATION:
        data[ADDNOTATION].append([int(coordinates[0]), int(coordinates[1]), int(coordinates[2]), int(coordinates[3])])
    elif coordinates[4] == FOOTER:
        data[FOOTER].append([int(coordinates[0]), int(coordinates[1]), int(coordinates[2]), int(coordinates[3])])
    else:
        data[PAGE_NR].append([int(coordinates[0]), int(coordinates[1]), int(coordinates[2]), int(coordinates[3])])

    # coordinates = [int(coordinates[0]), int(coordinates[1]), int(coordinates[2]), int(coordinates[3])]
    # data['columns'].append(coordinates)
    # elif data_type != 0:
    #     data['others'].append(coordinates)

json_data = json.dumps(data)

print("*****" + filename + "\n")

try:
    file_name = filename
    file = open("./../processed-images/" + file_name + ".json", "w")
    file.write(json_data)
    file.close()
except Exception as e:
    print(e)
    # print_retcode(retcode)
