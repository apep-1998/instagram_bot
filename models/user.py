#! /usr/bin/python
"""
    @Author_name : Arsham mohammadi nesyshabori
    @Author_email : arshammoh1998@gmail.com
    @Author_nickname : apep
    @date : 
    @version : 
"""
import settings as stng
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
        self.setting = {}

    def load_setting(self):
        with open(stng.USER_SETTING(self.username), 'r') as setting_file:
            self.setting = json.load(setting_file)

    