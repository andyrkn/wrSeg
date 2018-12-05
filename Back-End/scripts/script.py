import os
import sys
import re
import subprocess
import json

print(os.getcwd())
print(sys.argv)

filename = sys.argv[1].split('.')[-2]
extension = sys.argv[1].split('.')[-1]
# print(sys.argv[1].split('.'))
# f = open('./../processed-images/' + filename + '.json', 'w')
# f.write("{}\n")
# f.close()

try:
    res = subprocess.call('./bash-script ./../assets/' + filename + '.' + extension, shell = True)# + ' -o' + ' temp')
    print("\n\n\nHELLLLLLLLLLLO\n\n\n")
except Exception as e:
    print(e)

coordinates_file = open('column_indexes.txt','r')
coordinates_line = coordinates_file.readlines()
coordinates_file.close()
data=dict()
data['columns']=[]
data['others']=[]
data_type=0
for coordinates in coordinates_line :
    coordinates=coordinates.strip('\n').split(' ')
    # print(coordinates)
    coordinates=[int(coordinates[0]),int(coordinates[1]),int(coordinates[2]),int(coordinates[3])]
    data['columns'].append(coordinates)
    # elif data_type != 0:
    #     data['others'].append(coordinates)
json_data = json.dumps(data)

print("*****" + filename + "\n")

try:
    file_name=filename
    file = open("./../processed-images/" + file_name+ ".json" , "w")
    file.write(json_data)
    file.close();
except Exception as e:
    print(e)
    # print_retcode(retcode)