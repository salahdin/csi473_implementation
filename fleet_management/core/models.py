from django.db import models
from django.contrib.auth.models import User


class Vehicle(models.Model):
    vehicle_name = models.CharField(max_length=100, null=True)
    vehicle_type = models.CharField(max_length=100)
    vehicle_description = models.TextField(max_length=255)
    vehicle_Pnumber = models.CharField(max_length=7)
    color = models.CharField(max_length=100,verbose_name="vehicle color",null=True)
    photo = models.ImageField(upload_to='cars', null=True)


class Reservation(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name='vehicle_id', on_delete=models.CASCADE)
    customer = models.ForeignKey(User, related_name='Customer_id', on_delete=models.CASCADE)
    rent_from = models.DateTimeField(verbose_name="date rented")
    rent_to = models.DateField(verbose_name="date returned")


class ReturnVehicle(models.Model):
    customer = models.ForeignKey(User, related_name='return_Customer_id', on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, related_name='return_vehicle_id', on_delete=models.CASCADE)
    DOR = models.DateField(verbose_name="date returned")
    condition = models.CharField(max_length=200)
    mileage = models.DecimalField(max_digits=5, decimal_places=2)

