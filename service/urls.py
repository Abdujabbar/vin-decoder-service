from django.urls import path

from . import views

urlpatterns = [
    path('<str:vin>', views.vehicle_by_vin),
]
