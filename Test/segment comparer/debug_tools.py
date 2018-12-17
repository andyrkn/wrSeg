import os
import json
import cv2
import segment

def images_from_json(json_path, original_image_path):
    with open(json_path, "r") as fd:
        json_content = json.load(fd)

    print(json_content)
    print(json_content['columns'])

    original_image = cv2.imread(original_image_path)

    segment_images = []
    for column in json_content['columns']:
        segment_info = segment.SegmentInfo(original_image, (column[0], column[1]), column[2] - column[0], column[3] - column[1])
        segment_images += [segment_info.image]
    
    return segment_images

def write_images(images, folder_path):
    for i, image in enumerate(images):
        cv2.imwrite(os.path.join(folder_path, "segment {}.png".format(i)), image)

if __name__ == "__main__":
    images = images_from_json("./tests/json/testpage.json", "./tests/json/testpage.png")
    write_images(images, "./tests/json/result")


    