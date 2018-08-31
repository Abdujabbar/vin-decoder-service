from django.test import TestCase
from .decoder.decodethis import DecodeThisDecoder
from django.db import models
from .models import Vehicle
from django.conf import settings
from .helpers import gen_decode_this_url


class VehicleModelTest(TestCase):
    real_vin = "JT3GM84R2W0031533"

    def test_find_or_create(self):
        with self.assertRaises(models.ObjectDoesNotExist):
            Vehicle.objects.get(vin=self.real_vin)

        record = Vehicle.find_or_create(vin=self.real_vin)
        self.assertTrue(isinstance(record, Vehicle))

        stored_record = Vehicle.objects.get(vin=self.real_vin)

        self.assertEqual(stored_record, record)


class DecodeThisDecoderTest(TestCase):
    real_vin = "JF2SJAKC0FH514820"

    def test_decode(self):
        url = gen_decode_this_url(self.real_vin, settings.DECODE_API_KEY,
                                  settings.DECODE_THIS_JSON_FORMAT)
        try:
            decoder = DecodeThisDecoder(url, []).run()
            self.assertEqual(decoder['vin'], self.real_vin)
        except Exception as e:
            print(e)
