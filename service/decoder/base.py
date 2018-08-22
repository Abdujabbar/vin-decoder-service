from abc import ABC, abstractmethod


class BaseDecoder(ABC):
    def __init__(self, args):
        self.args = args

        self.validate_args()

    @abstractmethod
    def validate_args(self):
        """
        validates args on init class objects
        :return:
        """
        pass

    @abstractmethod
    def run(self):
        """
        Method will filling up an empty result of dictionary which generated in method make_an_empty_result
        :return dict:
        """
        pass

    def make_an_empty_result(self):
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