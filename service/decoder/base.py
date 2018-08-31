from abc import ABC, abstractmethod
from django.core.validators import URLValidator


class BaseDecoder(ABC):
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
    def run(self):
        """
        Method will filling up an empty result of dictionary
        which generated in method make_an_empty_result
        :return dict:
        """
        pass

    @staticmethod
    def make_an_empty_result():
        return dict(
            year="",
            model="",
            make="",
            type="",
            vin="",
            color="",
            weight=0,
            dimensions=""
        )

    @abstractmethod
    def launch_request(self):
        pass



