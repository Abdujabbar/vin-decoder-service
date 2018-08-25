from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import VehicleSerializer
from .transport.exceptions import NotFoundException, UnauthorizedException, InternalServerErrorException
from rest_framework import status
from .models import Vehicle


@api_view(['GET'])
def index(request, vin):
    try:
        serializer = VehicleSerializer(Vehicle().find_or_create(vin))
        return Response({
            "success": True,
            "vehicle": serializer.data,
        })
    except (NotFoundException, UnauthorizedException, InternalServerErrorException, Exception) as e:

        response_status = status.HTTP_401_UNAUTHORIZED

        if isinstance(e, NotFoundException):
            response_status = status.HTTP_404_NOT_FOUND
        else:
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR

        return Response({
            "success": False,
            "error": str(e)
        }, status=response_status)