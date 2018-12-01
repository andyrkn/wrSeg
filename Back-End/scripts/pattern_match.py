import cv2 #pip3 install opencv-python
import sys
import os

method = cv2.TM_SQDIFF_NORMED

def get_pattern_match_points(template , cutout):
    points_list = []
    large_image = cv2.imread(template)
    for elem in cutout:
        small_image = cv2.imread(elem)
        result = cv2.matchTemplate(small_image, large_image, method) #match with template
        mn,_,mnLoc,_ = cv2.minMaxLoc(result) #lowest point on match
        height,width = small_image.shape[:2]
        x_axis_match,y_axis_match = mnLoc
        points_list.append([x_axis_match,y_axis_match,height,width])
    return points_list


if __name__ == "__main__":
    if(len(sys.argv) > 1):
        if(sys.argv[1] == "-h"):
            print("pattern_match.py [full_image_path] [crop_image_path_1] [crop_image_path_2] or [dir_with_crop_images_path]")
            exit()
    else:
        print("Use -h for usage information")
        exit()
    try:
        data = []
        cutout_list = []
        if(os.path.isdir(sys.argv[2])):
            for entry in os.listdir(sys.argv[2]):
                if(entry.endswith(".png") and os.path.isfile(os.path.join(sys.argv[2] , entry))):
                    cutout_list.append(os.path.join(sys.argv[2] , entry))
        else:
            cutout_list = sys.argv[2:]
        data = get_pattern_match_points(sys.argv[1] , cutout_list)
        with open("train_data.txt" , "a") as fd:
            for match in data:
                for i in range(len(match) - 1):
                    fd.write(str(match[i]) + " ")
                fd.write(str(match[len(match) - 1]) + "\n")
    except Exception as e:
        print(e)

# Used for debugging
# trows,tcols = small_image.shape[:2]
# cv2.rectangle(large_image, (x_axis_match,y_axis_match),(x_axis_match+tcols,y_axis_match+trows),(0,0,255),2)
#
# cv2.imshow('output',large_image)
#
# # The image is only displayed if we call this
# cv2.waitKey(0)
