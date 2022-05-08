# serializers.py
from rest_framework import serializers

from .models import AirportData


class AirportDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AirportData
        fields = (
        'extract_date', 'report_period', 'terminal', 'arrival_departure', 'domestic_international', 'passenger_count')
