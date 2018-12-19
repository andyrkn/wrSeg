import os
import json
import cv2
import segment

def segment_image_from_2_points_coords(original_image, top_left, bot_right):
    """Create an image from segment coordinates and the original image

    Arguments:
        original_image {numpy.ndarray} -- The image from which the segment originates
        top_left {list/tuple/..} -- A list with the x and y coordinates of the top-left most corner
        bot_right {list/tuple/..} -- A list with the x and y coordinates of the bot-right most corner

    Returns:
        numpy.ndarray -- The resulting image
    """

    width = bot_right[0] - top_left[0]
    height = bot_right[1] - top_left[1]
    segment_info = segment.SegmentInfo(original_image, top_left, width, height)
    return segment_info.image

def images_dict_from_coords_dict(coords_dict, original_image_path):
    """Create a dictionary of images from a dictionary of segment coordinates
    
    Arguments:
        coords_dict {dict} -- A dictionary with the coordinates of the segments
        original_image_path {numpy.ndarray} -- The image from which the segments originate
    
    Returns:
        dict -- A dictionary of images
    """

    original_image = cv2.imread(original_image_path)
    images_dict = dict()

    for label in coords_dict:
        images_dict[label] = []
        for segment_coords in coords_dict[label]:
            top_left = (segment_coords[0], segment_coords[1])
            bot_right = (segment_coords[2], segment_coords[3])
            segment_image = segment_image_from_2_points_coords(original_image, top_left, bot_right)
            images_dict[label] += [segment_image]
    
    return images_dict

def images_dict_from_json_string(json_string, original_image_path):
    """"Create a dictionary of images from a json of segment coordinates
    
    Arguments:
        json_string {string} -- a json with the coordinates of the segments
        original_image_path {numpy.ndarray} -- The image from which the segments originate
    
    Returns:
        dict -- A dictionary of images
    """

    coords_dict = json.loads(json_string)
    return images_dict_from_coords_dict(coords_dict, original_image_path)

def images_dict_from_json_path(json_path, original_image_path):
    """Create a dictionary of images from a json of segment coordinates
    
    Arguments:
        json_path {string} -- The path to a json with the segment coordinates
        original_image_path {numpy.ndarray} -- The image from which the segments originate
    
    Returns:
        dict -- A dictionary of images
    """

    with open(json_path, "r") as fd:
        coords_dict = json.load(fd)
    return images_dict_from_coords_dict(coords_dict, original_image_path)

def write_images_from_dict(images_dict, folder_path):
    """Write images to disk from a dictionary of images
    
    Arguments:
        images_dict {dict} -- The dictionary containing the images
        folder_path {string} -- The folder path where the files will be created
    """

    for label in images_dict:
        for i, image in enumerate(images_dict[label]):
            image_path = os.path.join(folder_path, "{} {}.png".format(label, i))
            if not cv2.imwrite(image_path, image):
                print("Could not create image at: {}".format(image_path))


if __name__ == "__main__":
    images = images_dict_from_json_path("./tests/json/testpage.json", "./tests/json/testpage.png")
    write_images_from_dict(images, "./tests/json/result")
    