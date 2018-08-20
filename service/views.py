from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import VehicleSerializer

from .models import Vehicle


@api_view(['GET'])
def index(request, vin):
    try:
        serializer = VehicleSerializer(Vehicle().get_or_create(vin))
        return Response({
            "success": True,
            "vehicle": serializer.data,
        })
    except Exception as e:
        return Response({
            "success": False,
            "error": str(e)
        })
