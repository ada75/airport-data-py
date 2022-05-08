# models.py
from django.db import models


class AirportData(models.Model):
    extract_date = models.DateTimeField()
    report_period = models.DateTimeField()
    terminal = models.CharField(max_length=255)
    arrival_departure = models.CharField(max_length=255)
    domestic_international = models.CharField(max_length=255)
    passenger_count = models.PositiveIntegerField()

    def __str__(self):
        return self.report_period + self.terminal
