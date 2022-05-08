# views.py
from rest_framework import viewsets

from .serializers import AirportDataSerializer
from .models import AirportData


class AirportDataViewSet(viewsets.ModelViewSet):
    queryset = AirportData.objects.all().order_by('extract_date')
    serializer_class = AirportDataSerializer
