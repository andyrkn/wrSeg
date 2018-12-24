import os
import json

class CoordsTable:
    @staticmethod
    def from_coords_dict(coords_dict):
        coords_table = ""
        for label in coords_dict:
            for segment in coords_dict[label]:
                coords_table += "{} {} {} {}\n".format(segment[0], segment[1], segment[2], segment[3])
        return coords_table

    @staticmethod
    def from_json(json_string):
        coords_dict = json.loads(json_string)
        return CoordsTable.from_coords_dict(coords_dict)

    @staticmethod
    def from_json_path(json_path):
        with open(json_path, "r") as fd:
            json_string = fd.read()
        return CoordsTable.from_json(json_string)

if __name__ == "__main__":
    input_path = "../../jsons/m1.jpg.json"
    print(CoordsTable.from_json_path(input_path))
            