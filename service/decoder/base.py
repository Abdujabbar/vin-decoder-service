from abc import ABC, abstractmethod


class BaseDecoder(ABC):
    def __init__(self, args):
        self.args = args

        self.validate_args()

    @abstractmethod
    def validate_args(self):
        pass

    @abstractmethod
    def run(self):
        pass
