from .base import BaseDecoder
from .exceptions import *


class DecodeThisDecoder(BaseDecoder):

    def validate_args(self):
        if not self.args['decode']['status'] == 'SUCCESS' or \
                not type(self.args['decode']['vehicle']) is list or \
                len(self.args['decode']['vehicle']) == 0:
            raise BaseDecodeException("Invalid arguments passed")

    def run(self):
        data = self.args['decode']['vehicle'][0]

        result = dict(
            year="",
            model="",
            make="",
            type="",
            vin="",
            color="",
            weight=0,
            dimensions=""
        )

        result['year'] = data['year']
        result['model'] = data['model']
        result['make'] = data['make']
        result['type'] = data['body']
        result['vin'] = self.args['decode']['VIN']

        color_keys = ['Exterior Color', 'Interior Color']
        dimension_keys = ['Overall Width', 'Overall Length', 'Overall Height']
        weight_keys = ['Curb Weight-automatic']


        for equipment in data['Equip']:
            if equipment['name'] in color_keys:
                result['color'] += equipment['value']
            elif equipment['name'] in dimension_keys:
                result['dimensions'] += equipment['name'] + ':' + str(equipment['value']) + ' ' + equipment['unit'] + ';'
            elif equipment['name'] in weight_keys:
                result['weight'] = equipment['value']


        result['dimensions'] = result['dimensions'].strip('x')

        return result
