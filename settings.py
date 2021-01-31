from os import path

#project folder
BASE_DIR = path.dirname(__file__)

#project data folder
DATA_DIR = path.join(BASE_DIR, "data")

#
USER_SETTING = lambda username: path.join(DATA_DIR, username) if path.exists(path.join(DATA_DIR, username)) else None