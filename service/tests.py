from django.test import TestCase
import unittest
from .transport.decodethis import DecodeThisTransport
# Create your tests here.
class DecodeThisTransportTest(TestCase):
    def test_invalid_arguments(self):
        with self.assertRaises(Exception) as cm:
            DecodeThisTransport("", [])

        with self.assertRaises(Exception) as c:
            DecodeThisTransport("dsadsa", [])

