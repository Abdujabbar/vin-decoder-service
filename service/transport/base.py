from abc import abstractmethod
from django.core.validators import URLValidator


class BaseTransport:
    address = ""
    payload = []
    def __init__(self, address, payload):
        if not (type(address) is str) or len(address) == 0:
            raise Exception("address must be a string, and cannot be empty")

        if not (type(payload) is list):
            raise Exception("params must be instance of list")

        url_validator = URLValidator()

        url_validator(address)

        self.address = address
        self.payload = payload

    @abstractmethod
    def lunch_request(self):
        pass


