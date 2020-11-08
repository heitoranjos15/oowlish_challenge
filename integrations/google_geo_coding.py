import requests
from config import enviroment


def get_geo_code_by_address(address):
    params = {
        'key': enviroment.google_api_key,
        'address': address
    }
    response = requests.post(enviroment.google_host, params=params).json()

    if not response.get('results'):
        error_message = response.get('status')
        raise Exception(error_message)

    return response
