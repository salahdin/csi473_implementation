from django.db import models
from django.contrib.auth.models import User

type_options = [
    ('Student', 'Student'),
    ('Staff', 'Staff'),
]

# Create your models here
class Vehicle(models.Model):
    vehicle_name = models.CharField(max_length=100,null=True)
    vehicle_type = models.CharField(max_length=100)
    vehicle_description = models.TextField(max_length=255)
    vehicle_Pnumber = models.CharField(max_length=7)


    def __str__():
        return vehicle_name

class Reservation(models.Model):
    vehicle = models.ForeignKey(Vehicle,related_name='vehicle_id',on_delete=models.CASCADE)
    customer = models.ForeignKey(User ,related_name='Customer_id',on_delete=models.CASCADE)
    rent_from = models.DateTimeField()
    rent_to = models.DateField()

    def __str__():
        return rent_from + rent_to