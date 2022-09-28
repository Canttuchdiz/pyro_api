import requests
from exceptions import *

class Http:

    @staticmethod
    def get_request(url, header=None):
        payload = requests.get(url=str(url), header=header)
        status = payload.status_code
        if status is 200:
            data = payload.json()
            return data
        raise StatusCodeException(f"Invalid GET request: Error code {status}")
