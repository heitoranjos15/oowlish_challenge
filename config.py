import os


class Config():
    def __init__(self):
        self.google_host = 'https://maps.googleapis.com/maps/api/geocode/json?'


class Development(Config):
    def __init__(self):
        super().__init__()
        self.api_host = 'http://127.0.0.1:8000'
        self.google_api_key = 'AIzaSyCfilbhHnqXe2LLDpnn-atLxCd5AmkjAwk'


def __get_enviroment():
    env_value = os.environ.get('PYTHON_ENVIROMENT', 'dev')
    enviroments = {
        'dev': Development,
    }
    return enviroments[env_value]()


enviroment = __get_enviroment()
