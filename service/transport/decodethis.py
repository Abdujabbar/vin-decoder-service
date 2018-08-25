from .base import BaseTransport
from .exceptions import UnauthorizedException, \
                        NotFoundException, \
                        InternalServerErrorException, \
                        UnexpectedException
import requests
from rest_framework import status


class DecodeThisTransport(BaseTransport):
    def lunch_request(self):
        r = False
        try:
            r = requests.get(self.url, self.payload)
            r.raise_for_status()
        except requests.exceptions.RequestException:
            if r.status_code == status.HTTP_401_UNAUTHORIZED:
                raise UnauthorizedException()
            else:
                raise UnexpectedException()

        res = r.json()
        if res['decode']['status'] == 'SUCCESS':
            return res
        elif res['decode']['status'] == 'NOTFOUND':
            raise NotFoundException(res['decode']['status'])
        else:
            raise InternalServerErrorException(res['decode']['status'])
