import requests
import json

def json_from_path(image_path):
    url = "http://localhost:8082/upload-file"
    files = {'file': open(image_path, 'rb')}
    response = requests.post(url, files=files, verify=False)
    return response.text

def dict_from_path(image_path):
    json_string = json_from_path(image_path)
    return json.loads(json_string)

if __name__ == "__main__":
    image_path = './tests/json/testpage.png'
    print(type(json_from_path(image_path)))
    print(type(dict_from_path(image_path)))
