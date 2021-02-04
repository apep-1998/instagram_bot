import settings
import json

def to_json(python_object):
    if isinstance(python_object, bytes):
        return {'__class__': 'bytes',
                '__value__': codecs.encode(python_object, 'base64').decode()}
    raise TypeError(repr(python_object) + ' is not JSON serializable')


def from_json(json_object):
    if '__class__' in json_object and json_object['__class__'] == 'bytes':
        return codecs.decode(json_object['__value__'].encode(), 'base64')
    return json_object


def save_cookie(api, username):
    cache_settings = api.settings
    with open(settings.USER_SETTING("cookie_"+username+".cfg"), 'w') as outfile:
        json.dump(cache_settings, outfile, default=to_json)


def load_cookie(username):
    try:
        with open("cookie_"+username+".cfg") as file_data:
            cached_settings = json.load(file_data, object_hook=from_json)
        return cached_settings
    except Exception as e:
        print(e)
        return None