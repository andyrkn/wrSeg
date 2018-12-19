import requests
import json
import image_tools
import os

def json_from_path(image_path):
    url = "http://localhost:8082/upload-file"
    files = {'file': open(image_path, 'rb')}
    response = requests.post(url, files=files, verify=False)
    return response.text

def coords_dict_from_path(image_path):
    json_string = json_from_path(image_path)
    return json.loads(json_string)

def segment_images_from_path(image_path):
    coords_dict = coords_dict_from_path(image_path)
    segment_images = image_tools.images_dict_from_coords_dict(coords_dict, image_path)
    return segment_images

def segment_images_from_folder_path(folder_path):
    folder_dict = dict()
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            try:
                segment_images = segment_images_from_path(file_path)
                if segment_images:
                    folder_dict[file_name] = segment_images
                else:
                    print("{}: empty folder".format(file_name))
            except Exception as e:
                print("{}: exception: {}".format(file_name, e))
    return folder_dict

if __name__ == "__main__":
    # image_path = './tests/json/testpage.png'
    # folder_path = './tests/result'
    # segment_images = segment_images_from_path(image_path)
    # image_tools.write_images_from_dict(segment_images, folder_path)
    input_folder_path = './tests/images'
    output_folder_path = './tests/output_folder'
    folder_dict = segment_images_from_folder_path(input_folder_path)
    for folder_name in folder_dict:
        segments_folder_path = os.path.join(output_folder_path, folder_name)
        if not os.path.exists(segments_folder_path):
            os.makedirs(segments_folder_path)
        image_tools.write_images_from_dict(folder_dict[folder_name], segments_folder_path)
