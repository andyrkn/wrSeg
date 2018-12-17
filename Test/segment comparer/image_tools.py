import os
import json
import cv2
import segment

def segment_image_from_2_points_coords(original_image, top_left, bot_right):
    width = bot_right[0] - top_left[0]
    height = bot_right[1] - top_left[0]
    segment_info = segment.SegmentInfo(original_image, top_left, width, height)
    return segment_info.image

def images_dict_from_json(json_path, original_image_path):
    with open(json_path, "r") as fd:
        json_content = json.load(fd)

    original_image = cv2.imread(original_image_path)
    images_dict = dict()

    for label in json_content:
        images_dict[label] = []
        for segment_coords in json_content[label]:
            top_left = (segment_coords[0], segment_coords[1])
            bot_right = (segment_coords[2], segment_coords[3])
            segment_image = segment_image_from_2_points_coords(original_image, top_left, bot_right)
            images_dict[label] += [segment_image]
    
    return images_dict

def write_images_from_dict(images_dict, folder_path):
    for label in images_dict:
        for i, image in enumerate(images_dict[label]):
            cv2.imwrite(os.path.join(folder_path, "{} {}.png".format(label, i)), image)


if __name__ == "__main__":
    images = images_dict_from_json("./tests/json/testpage.json", "./tests/json/testpage.png")
    write_images_from_dict(images, "./tests/json/result")
    