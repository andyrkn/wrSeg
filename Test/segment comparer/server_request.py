import requests
import json
import image_tools
import os

class BadRequestException(Exception):
    def __init__(self, message, response=None):
        super().__init__(message)
        self.response = response

def json_from_path(image_path):
    url = "http://localhost:8082/upload-file"
    files = {'file': open(image_path, 'rb')}
    response = requests.post(url, files=files, verify=False)
    if response.ok:
        return response.text
    else:
        raise BadRequestException("Bad request", response=response)

def coords_dict_from_path(image_path):
    json_string = json_from_path(image_path)
    return json.loads(json_string)

def segment_images_from_path(image_path):
    coords_dict = coords_dict_from_path(image_path)
    segment_images = image_tools.images_dict_from_coords_dict(coords_dict, image_path)
    return segment_images

def segment_images_from_folder_path(folder_path, on_success_listeners=None):
    folder_dict = dict()
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            print("{}:".format(file_name))
            try:
                segment_images = segment_images_from_path(file_path)
                if segment_images:
                    folder_dict[file_name] = segment_images
                    print("successful")
                    if on_success_listeners:
                        for listener in on_success_listeners:
                            listener(file_name, segment_images)
                else:
                    print("empty folder")
            except BadRequestException as e:
                print("bad request:\n{}".format(e.response.text))
            except Exception as e:
                print("exception: {}".format(e))
    return folder_dict


if __name__ == "__main__":
    # image_path = './tests/images/m18.png'
    # folder_path = './tests/result'
    # segment_images = segment_images_from_path(image_path)
    # image_tools.write_images_from_dict(segment_images, folder_path)
    pass