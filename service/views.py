from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import models
from .transport.decodethis import DecodeThisTransport
from .decoder.decodethis import *
from .serializers import VehicleSerializer

from django.conf import settings

from .models import Vehicle


@api_view(['GET'])
def index(request, vin):
    try:
        record = Vehicle.objects.get(vin=vin)
        serializer = VehicleSerializer(record)
        return Response({
            "success": True,
            "vehicle": serializer.data
        })
    except models.ObjectDoesNotExist as e:
        print("ExceptionMessage %s" % e)

    try:
        transport = DecodeThisTransport(settings.DECODE_THIS_URL %
                                        (
                                            vin,
                                            settings.DECODE_API_KEY,
                                            settings.DECODE_THIS_JSON_FORMAT
                                        ), [])

        data = transport.lunch_request()
        vehicle_dict = DecodeThisDecoder(data).run()
        record = Vehicle.objects.create(**vehicle_dict)
        serializer = VehicleSerializer(record)
        return Response({
            "success": True,
            "vehicle": serializer.data,
        })

    except Exception as e:
        return Response({
            "success": False,
            "error": str(e),
        })
