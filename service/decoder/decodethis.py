from .base import BaseDecoder
from .exceptions import *


class DecodeThisDecoder(BaseDecoder):
    color_keys = ['Exterior Color', 'Interior Color']
    dimension_keys = ['Overall Width', 'Overall Length', 'Overall Height']
    weight_keys = ['Curb Weight-automatic']

    def validate_args(self):
        if not isinstance(self.args, dict) or \
                not 'decode' in self.args.keys() or \
                len(self.args['decode']['vehicle']) == 0:
            raise BaseDecodeException("Invalid arguments passed")

    def run(self):

        data = self.args['decode']['vehicle'][0]

        result = self.make_an_empty_result()

        result['year'] = data['year']
        result['model'] = data['model']
        result['make'] = data['make']
        result['type'] = data['body']
        result['vin'] = self.args['decode']['VIN']

        for equipment in data['Equip']:
            if equipment['name'] in self.color_keys:
                result['color'] += equipment['value']
            elif equipment['name'] in self.dimension_keys:
                result['dimensions'] += equipment['name'] + ':' + str(equipment['value']) + ' ' + equipment[
                    'unit'] + ';'
            elif equipment['name'] in self.weight_keys:
                result['weight'] = equipment['value']

        result['dimensions'] = result['dimensions'].strip('x')

        return result
