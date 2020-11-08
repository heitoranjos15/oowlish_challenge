import os


class Config():
    def __init__(self):
        self.google_host = 'https://maps.googleapis.com/maps/api/geocode/json?'


class Development(Config):
    def __init__(self):
        super().__init__()
        self.google_api_key = 'AIzaSyCfilbhHnqXe2LLDpnn-atLxCd5AmkjAwk'


def __get_enviroment():
    env_value = os.environ.get('ENVIROMENT', 'dev')
    enviroments = {
        'dev': Development,
    }
    return enviroments[env_value]()


enviroment = __get_enviroment()
