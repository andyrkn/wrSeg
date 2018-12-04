from PIL import Image
import numpy as np


intervals = {}


def read_intervals():
	fd = open("intervals.txt",'r')
	lines = fd.readlines()
	for line in lines:
		data = line.strip().split(' ')
		intervals[(int(data[0]),int(data[1]))] = []

read_intervals()

def read_data():
	fd = open("test_data.txt", 'r')
	lines = fd.readlines()
	for line in lines:
		data = line.split(' ')
		for interval in intervals:
			if  (interval[0] <= int(data[1]) and interval[1] >= int(data[1])  ) or  (interval[0] <= int(data[1]) + int(data[3]) and interval[1] >= int(data[1]) + int(data[3]) ):
				intervals[interval].append((int(data[2]), int(data[1]), int(data[2]) + int(data[4]), int(data[1]) + int(data[3]) ))
				# coordinates.append( (int(data[2]), int(data[1]), int(data[2]) + int(data[4]), int(data[1]) + int(data[3]) ) )
	# print(coordinates)

read_data()


# for interval in intervals:
# 	print(interval)
# 	print(intervals[interval])


def view_image():
	img = Image.open("/home/oanabzz/Desktop/testpage.png")
	index = 1
	for coordinate in coordinates:
		img2 = img.crop(coordinate)
		name = "img" + str(index) + ".jpg"
		index = index +1
		img2.save(name)
# view_image()

def sort_coordinates_by_ox():
	global intervals
	for coordinates in intervals:
		intervals[coordinates].sort(key = lambda x : x[0])

columns = {}
threshold = 0.15

def is_in_columns(interval):
	for key in columns:
		if interval[0] > key[0] and interval[1] < key[1]:
			return key
	return False

def get_columns_practic_proiectul():
	global columns
	for intr in intervals:
		coordinates = intervals[intr]
		for line in coordinates:
			interval = (line[0], line[2])
			key = is_in_columns(interval)
			padding =  threshold * (line[2] - line[0])
			if key == False:
				interval = tuple((interval[0] - padding, interval[1] + padding))
				columns[interval] = [line]
			else:
				columns[key].append(line)


# for key in columns:
# 	print(key)
	#print(columns[key])

def crop_pic(x1,y1,x2,y2,name):
	img = Image.open("/home/oanabzz/Desktop/test-layout.png")
	img2 = img.crop((x1,y1,x2,y2))
	img2.save(name)


def view_columns():
	i=1
	for column in columns.values():
		x1_max, y1_max, x2_max, y2_max = np.amax(column,axis=0)
		x1_min, y1_min, x2_min, y2_min = np.amin(column,axis=0)
		crop_pic(x1_min, y1_min, x2_max, y2_max, "column{}.png".format(str(i)))
		i = i+1

	# for column in columns.values():
	# 	x0 = min([line[0] for line in column])
	# 	y0 = min([line[1] for line in column])
	# 	x1 = max([line[2] for line in column])
	# 	y1 = max([line[3] for line in column])
	# 	print(str(x0) + " " + str(y0) + " " + str(x1) + " " + str(y1))

get_columns_practic_proiectul()
view_columns()