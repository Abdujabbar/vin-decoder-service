from .base import BaseDecoder
from .exceptions import BaseDecodeException


class DecodeThisDecoder(BaseDecoder):

    color_keys = ['Exterior Color', 'Interior Color']
    dimension_keys = ['Overall Width', 'Overall Length',
                      'Overall Height']
    weight_keys = ['Curb Weight-automatic']

    def validate_args(self):
        if not isinstance(self.args, dict) or \
           'decode' not in self.args.keys() or \
           len(self.args['decode']['vehicle']) == 0:
            raise BaseDecodeException('Invalid arguments passed')

    def run(self):
        vehicle_data = self.args['decode']['vehicle'][0]
        result = self.make_an_empty_result()
        result['year'] = vehicle_data['year']
        result['model'] = vehicle_data['model']
        result['make'] = vehicle_data['make']
        result['type'] = vehicle_data['body']
        result['vin'] = self.args['decode']['VIN']
        result['color'] = self.collect_color_info(vehicle_data['Equip'])

        result['dimensions'] = self.collect_dimensions_info(
            vehicle_data['Equip']
        )

        result['weight'] = self.collect_weight_info(vehicle_data['Equip'])
        return result

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
                result = equipment['value']
        return result

    def collect_dimensions_info(self, equipments):
        result = ''
        for equipment in equipments:
            if equipment['name'] in self.dimension_keys:
                result += equipment['name'] + ':' \
                    + str(equipment['value']) + ' ' + equipment['unit'] + ';'
        return result
