import os
import image_tools
import server_request

def create_segments_folder(folder_path, folder_name, segments_dict):
    segments_folder_path = os.path.join(folder_path, folder_name)
    if not os.path.exists(segments_folder_path):
        os.makedirs(segments_folder_path)
    image_tools.write_images_from_dict(segments_dict, segments_folder_path)

if __name__ == "__main__":
    input_folder_path = './tests/images'
    output_folder_path = './tests/output_folder'
    on_success_listeners = [lambda x, y: create_segments_folder(output_folder_path, x, y)]
    folder_dict = server_request.segment_images_from_folder_path(input_folder_path, on_success_listeners)