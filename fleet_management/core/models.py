from django.db import models


class Vehicle(models.Model):
    vehicle_id = models.IntegerField()
    vehicle_type = models.CharField(max_length=100)
    vehicle_description = models.TextField(max_length=255)
    vehicle_Pnumber = models.CharField(max_length=7)