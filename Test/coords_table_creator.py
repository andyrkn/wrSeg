import sys
import os
import adapters

def create_from_file(file_path):
    content = adapters.CoordsTable.from_json_path(file_path)
    output_file_name = os.path.splitext(os.path.basename(file_path))[0] + ".txt"
    with open(output_file_name, "w") as fd:
        fd.write(content)

def create_from_folder(folder_path):
    output_folder_name = "output " + os.path.basename(folder_path)
    if not os.path.exists(output_folder_name):
        os.makedirs(output_folder_name)

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            content = adapters.CoordsTable.from_json_path(file_path)
            output_file_name = os.path.splitext(os.path.basename(file_path))[0] + ".txt"
            
            with open(os.path.join(output_folder_name, output_file_name), "w") as fd:
                fd.write(content)

if __name__ == "__main__":
    if os.path.isfile(sys.argv[1]):
        create_from_file(sys.argv[1])
    if os.path.isdir(sys.argv[1]):
        create_from_folder(sys.argv[1])
