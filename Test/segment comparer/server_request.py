import requests
import json
import image_tools
import cv2

def json_from_path(image_path):
    url = "http://localhost:8082/upload-file"
    files = {'file': open(image_path, 'rb')}
    response = requests.post(url, files=files, verify=False)
    return response.text

def dict_from_path(image_path):
    json_string = json_from_path(image_path)
    return json.loads(json_string)

def segment_images_from_path(image_path, folder_path):
    coords_dict = dict_from_path(image_path)
    segment_images = image_tools.images_dict_from_coords_dict(coords_dict, image_path)
    return segment_images

if __name__ == "__main__":
    image_path = './tests/json/testpage.png'
    folder_path = './tests/result'
    segment_images = segment_images_from_path(image_path, folder_path)
    image_tools.write_images_from_dict(segment_images, folder_path)
