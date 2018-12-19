def diff(img1, img2):
	name1, x1, y1, h1, w1 = img1
	name2, x2, y2, h2, w2 = img2
	return max(abs(w2 - w1), abs(h2 - h1))

def minDist(img, imgList):
	name, x, y, h, w = img
	bot, top = 1e9, 1e9

	for img1 in imgList:
		name1, x1, y1, h1, w1 = img1
		if x1 + w1 < x or x1 > x + w: continue
		if y > y1 + h1: top = min(top, y - y1 - h1)
		elif y + h < y1: bot = min(bot, y1 - y - h)

	return min(top, bot) if min(top, bot) < 1e5 else 0

# with open("test_data.txt", "r") as inFile, open("test_data2.txt", "w") as outFile:
# 	images = inFile.readlines()
# 	for i in range(len(images)):
# 		strings = images[i].split()
# 		images[i] = [strings[0]] + list(map(int, strings[1:]))
#
# 	v = [0] * len(images)
#
# 	for i in range(len(images)):
# 		v[i] = minDist(images[i], images) * 100
# 		for j in range(len(images)):
# 			v[i] += diff(images[i], images[j])
#
# 	print(v)
# 	mean = sum(v) / len(v)
# 	print(mean)
# 	v = list(enumerate(v))
# 	v.sort()
# 	abberantValues = list(filter(lambda x: abs(x[1] - mean) / mean > 0.5, v))
# 	content = list(filter(lambda x: abs(x[1] - mean) / mean <= 0.5, v))
#
# 	xmin, xmax, ymin, ymax = 1e9, -1e9, 1e9, -1e9
# 	for img in content:
# 		x, y, h, w = images[img[0]][1:]
# 		xmin = min(xmin, x)
# 		xmax = max(xmax, x + w)
# 		ymin = min(ymin, y)
# 		ymax = max(ymax, y + h)
#
# 	print(xmin)
# 	print(xmax)
# 	print(ymin)
# 	print(ymax)
#
# 	for img in abberantValues:
# 		x, y, h, w = images[img[0]][1:]
#
# 		t = ""
# 		if y > ymax: t = "footer"
# 		else: t = "title"
# 		print(images[img[0]][0], img[1], t)
