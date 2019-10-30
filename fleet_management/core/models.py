from django.db import models


type_options = [
    ('Student', 'Student'),
    ('Staff', 'Staff'),
]

# Create your models here.
class Customer(models.Model):
    user_first_name = models.CharField(max_length =100) #edit the class
    user_last_name = models.CharField(max_length=100)
    user_email = models.CharField(max_length =200)
    user_DOB = models.DateField()
    user_type = models.CharField(max_length =100, choices = type_options)

class Vehicle(models.Model):
    vehicle_name = models.CharField(max_length=100,null=True)
    vehicle_type = models.CharField(max_length=100)
    vehicle_description = models.TextField(max_length=255)
    vehicle_Pnumber = models.CharField(max_length=7)

class Reservation(models.Model):
    vehicle = models.ForeignKey(Vehicle,related_name='vehicle_id',on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,related_name='Customer_id',on_delete=models.CASCADE)
    rent_from = models.DateTimeField()
    rent_to = models.DateField()