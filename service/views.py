from .decoder.exceptions import NotFoundException, UnauthorizedException
from .models import Vehicle
from django.http import JsonResponse


def vehicle_by_vin(request, vin):
    try:
        raw = Vehicle().find_or_create(vin)
        return JsonResponse({
            "success": True,
            "data": raw,
        })
    except Exception as e:
        response_code = 500

        if isinstance(e, NotFoundException):
            response_code = 404
        elif isinstance(e, UnauthorizedException):
            response_code = 401

        return JsonResponse({
            "status": "error",
            "message": str(e)
        }, status=response_code)