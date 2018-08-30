from abc import abstractmethod
from django.core.validators import URLValidator


class BaseTransport:
    url = ""
    payload = []

    def __init__(self, url, payload):
        if not (type(url) is str) or len(url) == 0:
            raise ValueError(
                "url address must be a string, and cannot be empty"
            )

        if not (type(payload) is list):
            raise ValueError("params must be instance of list")

        url_validator = URLValidator()

        url_validator(url)

        self.url = url
        self.payload = payload

    @abstractmethod
    def launch_request(self):
        pass
