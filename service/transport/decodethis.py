from .base import BaseTransport
from .exceptions import *
import requests


class DecodeThisTransport(BaseTransport):
    def lunch_request(self):
        r = False
        try:
            r = requests.get(self.url, self.payload)
            r.raise_for_status()
        except requests.exceptions.RequestException:
            pass

        res = r.json()

        if res['decode']['status'] == 'SUCCESS':
            return res

        if res['decode']['status'] == "NOTFOUND":
            raise NotFoundException(res['decode']['status'])
        elif res['decode']['status'] == "SECERR":
            raise UnauthorizedException()
        else:
            raise InternalServerErrorException(res['decode']['status'])
