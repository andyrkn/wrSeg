import os
import image_tools
import server_request

def create_segments_folder(folder_path, folder_name, segments_dict):
    """Create a folder and fill it with the images in a dictionary, 
    each image will be named in this format "<label> <i>.png",
    where <label> will be the key in the dictionary
    and <i> an incremented number.
    
    Arguments:
        folder_path {string} -- The path in where the root folder will be created
        folder_name {string} -- The name of the root folder
        segments_dict {string} -- A dictionary of lists of images
    """

    segments_folder_path = os.path.join(folder_path, folder_name)
    if not os.path.exists(segments_folder_path):
        os.makedirs(segments_folder_path)
    image_tools.write_images_from_dict(segments_dict, segments_folder_path)

def create_json_folder(input_folder_path, output_folder_path):
    for image_name in os.listdir(input_folder_path):
        image_path = os.path.join(input_folder_path, image_name)
        if os.path.isfile(image_path):
            print(image_name)
            try:
                json_string = server_request.json_from_path(image_path)
                with open(os.path.join(output_folder_path, image_name + ".json"), "w") as fd:
                    fd.write(json_string)
            except server_request.BadRequestException as e:
                print(e.response)
    

if __name__ == "__main__":
    input_folder_path = './images/1'
    output_folder_path = './tests/output_folder'
    #on_success_listeners = [lambda x, y: create_segments_folder(output_folder_path, x, y)]
    #folder_dict = server_request.segment_images_from_folder_path(input_folder_path, on_success_listeners)
    create_json_folder(input_folder_path, output_folder_path)