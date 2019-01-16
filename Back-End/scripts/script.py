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

THRESHOLD = "0.2"
# USEGAUSS = "false"
NOISE = "8"
MAXCOLSEPS = "100"
MINSCALE = "0"
MAXLINES = "1000"
MAXSEPS = "100"

filename = sys.argv[1].split('.')[-2]
extension = sys.argv[1].split('.')[-1]

# print(sys.argv[1].split('.'))
# f = open('./../processed-images/' + filename + '.json', 'w')
# f.write("{}\n")
# f.close()

if sys.argv[2] != "null":
    THRESHOLD = sys.argv[2]
if sys.argv[4] != "null":
    NOISE = sys.argv[4]
if sys.argv[5] != "null":
    MAXCOLSEPS = sys.argv[5]
if sys.argv[6] != "null":
    MINSCALE = sys.argv[6]
if sys.argv[7] != "null":
    MAXLINES = sys.argv[7]
if sys.argv[8] != "null":
    MAXSEPS = sys.argv[8]

try:
    res = subprocess.call(
        './bash-script ' + filename + " " + "./../assets/" + filename + '.' + extension + " " + THRESHOLD + " " + NOISE + " " + MAXCOLSEPS +
        " " + MINSCALE + " " + MAXLINES + " " + MAXSEPS, shell=True)  # + ' -o' + ' temp')
except Exception as e:
    print(e)

column_indexes_file = "../out/" + filename + ".txt"

coordinates_file = open(column_indexes_file, 'r')
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


try:
    file_name = filename
    file = open("./../processed-images/" + file_name + ".json", "w")
    file.write(json_data)
    file.close()
except Exception as e:
    print(e)
    # print_retcode(retcode)
