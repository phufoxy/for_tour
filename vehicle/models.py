from django.db import models
from datetime import datetime
from tourer.models import Tourer
from django.urls import reverse
# Create your models here.
class Type_vehicle(models.Model):
    type_vehicle = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('IndexView_Type_vehicle')

    def __str__(self):
        return self.type_vehicle

class City(models.Model):
    city = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('IndexView_Vehicle_City')

    def __str__(self):
        return self.city + '-' + self.address

class Vehicle(models.Model):
    type_vehicle = models.ForeignKey(Type_vehicle,on_delete=models.CASCADE)
    name_vehicle = models.CharField(max_length=250)
    garage = models.CharField(max_length=250)
    img_vehicle = models.FileField(upload_to = 'vehicle/',default='/default/user-avatar-default-165.png')
    location = models.ForeignKey(City,on_delete=models.CASCADE)
    review = models.IntegerField(default=0)
    star = models.FloatField(default=0)
    
    def get_absolute_url(self):
        return reverse('IndexView_vehicle')

    def __str__(self):
        return self.name_vehicle + '-' + self.location.city

class Vehicle_details(models.Model):
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    go_route = models.CharField(max_length=250)
    price = models.FloatField(default=0)
    img_route = models.FileField(upload_to='vehicle/',default='/default/user-avatar-default-165.png')

    def get_absolute_url(self):
        return reverse('IndexView_vehicle_details')

    def __str__(self):
        return self.vehicle.name_vehicle + '-' + self.go_route

class Car_details(models.Model):
    car = models.ForeignKey(Vehicle_details,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    start_status = models.CharField(max_length=5000)
    end_status = models.CharField(max_length=5000)
    img_status = models.FileField(upload_to='vehicle/',default='/default/user-avatar-default-165.png')

    def get_absolute_url(self):
        return reverse('IndexView_car')

    def __str__(self):
        return self.title + '-' + self.car.go_route

class Comment_Vehicle(models.Model):
    vehicle = models.ForeignKey(Vehicle_details, on_delete=models.CASCADE)
    commnet = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now())
    account = models.ForeignKey(Tourer,on_delete=models.CASCADE)

# class Vehicle_Tour(models.Model):
#     vehicle = models.ForeignKey(Vehicle_details,on_delete=models.CASCADE)
#     account = models.ForeignKey(Tourer,on_delete=models.CASCADE)
#     date = models.DateTimeField(default=datetime.now())
