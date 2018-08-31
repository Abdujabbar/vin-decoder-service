from .base import BaseDecoder
from .exceptions import UnauthorizedException, \
    UnexpectedException, \
    InternalServerErrorException, \
    NotFoundException
import requests
from rest_framework import status


class DecodeThisDecoder(BaseDecoder):
    color_keys = ['Exterior Color', 'Interior Color']
    dimension_keys = ['Overall Width', 'Overall Length',
                      'Overall Height']
    weight_keys = ['Curb Weight-automatic', 'Curb Weight-manual']

    def collect_color_info(self, equipments):
        result = ''
        for equipment in equipments:
            if equipment['name'] in self.color_keys:
                result += equipment['value']
        return result

    def collect_weight_info(self, equipments):
        result = 0
        for equipment in equipments:
            if equipment['name'] in self.weight_keys:
                result += float(equipment['value'])
        return result

    def collect_dimensions_info(self, equipments):
        result = ''
        for equipment in equipments:
            if equipment['name'] in self.dimension_keys:
                result += equipment['name'] + ':' \
                          + str(equipment['value']) + ' ' + equipment['unit'] + ';'
        return result

    def launch_request(self):
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

    def run(self):
        response_data = self.launch_request()

        vehicle_data = response_data['decode']['vehicle'][0]
        result = self.make_an_empty_result()
        result['year'] = vehicle_data['year']
        result['model'] = vehicle_data['model']
        result['make'] = vehicle_data['make']
        result['type'] = vehicle_data['body']
        result['vin'] = response_data['decode']['VIN']
        result['color'] = self.collect_color_info(vehicle_data['Equip'])

        result['dimensions'] = self.collect_dimensions_info(
            vehicle_data['Equip']
        )

        result['weight'] = self.collect_weight_info(vehicle_data['Equip'])
        return result
