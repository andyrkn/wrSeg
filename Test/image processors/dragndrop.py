import os
import cv2

def drop_file(file_path, action):
    image = cv2.imread(file_path)
    new_image = action(image)
    cv2.imwrite(os.path.basename(file_path), new_image)

def drop_folder(folder_path, action):
    output_folder = "output {}".format(os.path.basename(folder_path))
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    for image_name in os.listdir(folder_path):
        image_path = os.path.join(folder_path, image_name)
        image = cv2.imread(image_path)
        new_image = action(image)
        output_image = os.path.join(output_folder, os.path.basename(image_path))
        cv2.imwrite(output_image, new_image)
        
def drop(path, action):
    if os.path.isfile(path):
        drop_file(path, action)
    if os.path.isdir(path):
        drop_folder(path, action)