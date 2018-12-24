import os
import json

def from_coords_dict(coords_dict):
    coords_table = ""
    for label in coords_dict:
        for segment in coords_dict[label]:
            coords_table += "{} {} {} {}\n".format(segment[0], segment[1], segment[2], segment[3])
    return coords_table

def from_json(json_string):
    coords_dict = json.loads(json_string)
    return from_coords_dict(coords_dict)

def from_json_path(json_path):
    with open(json_path, "r") as fd:
        json_string = fd.read()
    return from_json(json_string)