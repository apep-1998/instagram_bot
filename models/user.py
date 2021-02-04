#! /usr/bin/python
"""
    @Author_name : Arsham mohammadi nesyshabori
    @Author_email : arshammoh1998@gmail.com
    @Author_nickname : apep
    @date : 
    @version : 
"""
from instagram_private_api import Client, ClientCompatPatch
import settings as stng
from tools import config, cookies
from functools import partial
import json

class User(object):
    user_list = []

    @classmethod
    def add_new_user(cls, username):
        setting_file = stng.USER_SETTING(username)
        for user in User.user_list:
            if user.username == username:
                print("user tekrari ast!")
                return

        if setting_file:
            User.user_list.append(User(username))
        else:
            print("setting user peyda nashod username -->  {}".format(username))


    def __init__(self, username):
        self.username = username
        self.setting = partial(config.get_key, file_name=stng.USER_SETTING(username))
        self.load_setting()
        self.make_api()

    def make_api(self):
        saved_cookie = cookies.load_cookie(self.username)
        self.api = Client(self.setting("username"), self.setting("password"))


