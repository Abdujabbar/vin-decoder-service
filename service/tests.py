from django.core.exceptions import ValidationError
import unittest
from django.test import TestCase
from .transport.decodethis import DecodeThisTransport
from .transport.exceptions import *
from .decoder.decodethis import *
from django.conf import settings
from django.db import models
from .models import Vehicle


class DecodeThisTransportTest(unittest.TestCase):
    invalid_vin = "11111"
    real_vin = "JF2SJAKC0FH514820"

    def test_arguments_validation(self):
        self.assertRaises(ValueError, DecodeThisTransport, url="", payload=[])
        self.assertRaises(ValueError, DecodeThisTransport, url="adsadsa", payload=None)
        self.assertRaises(ValidationError, DecodeThisTransport, url="adsadsa", payload=[])

    def test_not_found_exception(self):
        url = settings.DECODE_THIS_URL % (
            self.invalid_vin,
            settings.DECODE_API_KEY,
            settings.DECODE_THIS_JSON_FORMAT
        )
        transport = DecodeThisTransport(url, [])
        with self.assertRaises(NotFoundException):
            transport.lunch_request()

    def test_unauthorized_exception(self):
        url = settings.DECODE_THIS_URL % (
            self.real_vin,
            "dsadsada",
            settings.DECODE_THIS_JSON_FORMAT
        )
        transport = DecodeThisTransport(url, [])
        with self.assertRaises(UnauthorizedException):
            transport.lunch_request()

    def test_internal_error_exception(self):
        url = settings.DECODE_THIS_URL % (
            "543543543543543",
            settings.DECODE_API_KEY,
            settings.DECODE_THIS_JSON_FORMAT
        )
        transport = DecodeThisTransport(url, [])
        with self.assertRaises(InternalServerErrorException):
            transport.lunch_request()


class VehicleModelTest(TestCase):
    real_vin = "JT3GM84R2W0031533"

    def test_get_or_create(self):
        with self.assertRaises(models.ObjectDoesNotExist):
            Vehicle.objects.get(vin=self.real_vin)

        record = Vehicle.get_or_create(vin=self.real_vin)
        self.assertTrue(isinstance(record, Vehicle))

        stored_record = Vehicle.objects.get(vin=self.real_vin)

        self.assertEqual(stored_record, record)



class DecodeThisDecoderTest(TestCase):
    real_vin = "JF2SJAKC0FH514820"
    def test_invalid_args(self):
        args = {}
        self.assertRaises(BaseDecodeException, DecodeThisDecoder, args=args)

    def test_decode(self):
        url = settings.DECODE_THIS_URL % (
            self.real_vin,
            settings.DECODE_API_KEY,
            settings.DECODE_THIS_JSON_FORMAT
        )
        transport = DecodeThisTransport(url, [])

        try:
            data = transport.lunch_request()
            decoder = DecodeThisDecoder(data)

            self.assertEqual(decoder['vin'], self.real_vin)

        except Exception as e:
            print(e)