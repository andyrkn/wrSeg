import requests
import json
import image_tools
import os

class BadRequestException(Exception):
    def __init__(self, message, response=None):
        super().__init__(message)
        self.response = response

def json_from_path(image_path):
    """Request segmentation for an image and get json
    
    Arguments:
        image_path {string} -- The path for the image that will be segmented
    
    Raises:
        BadRequestException -- Exeption raised when the server could not segment the specified image
    
    Returns:
        string -- A json with the label and coordinates of each segment
    """

    url = "http://localhost:8082/upload-file"
    files = {'file': open(image_path, 'rb')}
    response = requests.post(url, files=files, verify=False)
    if response.ok:
        return response.text
    else:
        raise BadRequestException("Bad request", response=response)

def coords_dict_from_path(image_path):
    """Request segmentation for an image and get coordinates for each segment
    
    Arguments:
        image_path {string} -- The path for the image that will be segmented

    Raises:
        BadRequestException -- Exeption raised when the server could not segment the specified image
    
    Returns:
        dict -- a dictionary, key: label, value: a list of [top_left.x, top_left.y, bot_right.x, bot_right.y] for each segment
    """

    json_string = json_from_path(image_path)
    return json.loads(json_string)

def segment_images_from_path(image_path):
    """Request segmentation for an image and create a image for each segment
    
    Arguments:
        image_path {string} -- The path for the image that will be segmented

    Raises:
        BadRequestException -- Exeption raised when the server could not segment the specified image
    
    Returns:
        dict -- a dictionary, key: label, value: a list of all segments of that label
    """

    coords_dict = coords_dict_from_path(image_path)
    segment_images = image_tools.images_dict_from_coords_dict(coords_dict, image_path)
    return segment_images

def segment_images_from_folder_path(folder_path, on_success_listeners=None):
    """ Create segments for each image found in the folder
    
    Arguments:
        folder_path {string} -- a folder with the images to be segmented
    
    Keyword Arguments:
        on_success_listeners {bool} -- [events called when an image is successfully segmented] (default: {None})
    
    Returns:
        dict -- PLACEHOLDER empty dict (to save memory), use on_success_listeners to access images
    """

    folder_dict = dict()
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            print("{}:".format(file_name))
            try:
                segment_images = segment_images_from_path(file_path)
                if segment_images:
                    #folder_dict[file_name] = segment_images
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