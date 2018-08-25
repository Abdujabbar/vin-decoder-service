from django.db import models
from .transport.decodethis import DecodeThisTransport
from .decoder.decodethis import DecodeThisDecoder
from django.conf import settings
from .helpers import gen_decode_this_url


class Vehicle(models.Model):
    vin = models.CharField(max_length=17, unique=True, blank=False)
    year = models.IntegerField()
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    dimensions = models.CharField(max_length=100)
    weight = models.FloatField(default=0)

    def __str__(self):
        return self.vin

    @staticmethod
    def find_or_create(vin):
        try:
            record = Vehicle.objects.get(vin=vin)
            return record
        except models.ObjectDoesNotExist:

            generated_url = gen_decode_this_url(vin, settings.DECODE_API_KEY, settings.DECODE_THIS_JSON_FORMAT)

            transport = DecodeThisTransport(generated_url, [])
            data = transport.lunch_request()

            vehicle_dict = DecodeThisDecoder(data).run()

            return Vehicle.objects.create(**vehicle_dict)
