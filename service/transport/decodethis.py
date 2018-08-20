from .base import BaseTransport
import requests


class DecodeThisTransport(BaseTransport):
    def lunch_request(self):
        try:
            r = requests.get(self.address, self.payload)
            r.raise_for_status()
        except requests.exceptions.RequestException as err:
            raise err

        res = r.json()

        if res['decode']['status'] != "SUCCESS":
            raise Exception("Third party exception: %s" % res['decode']['status'])

        return res
