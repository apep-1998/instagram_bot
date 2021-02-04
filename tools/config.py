from settings import DATA_DIR
from os import path
import json


def get_key(key, file_name):
    out = None
    try:
        with open(path.join(DATA_DIR, file_name), "r") as setting_file:
            out = json.load(setting_file)
    except Exception as e:
        print(e)

    out = json.get(key)
    return out

def set_key(key, value, file_name):
    data = {}
    try:
        with open(path.join(DATA_DIR, file_name), "r") as setting_file:
            data = json.load(setting_file)
    except Exception as e:
        print(e)

    data[key] = value
    with open(path.join(DATA_DIR, file_name), "w") as setting_file:
        json.dump(data, setting_file)
