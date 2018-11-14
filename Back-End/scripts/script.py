import sys

file = open("./../processed-images/" + sys.argv[1] + ".json" , "w+")
file.write('{"info":"data about image"}')
file.close();

print(str(sys.argv[1]))