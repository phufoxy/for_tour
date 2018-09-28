from django.db import models
from datetime import datetime
from tourer.models import Tourer
from django.urls import reverse
from places.models import Place
from house.models import House
from restaurants.models import Restaurant
from vehicle.models import Vehicle_details
# Create your models here.
class Book_Tour(models.Model):
    name_book = models.CharField(max_length=250)
    date_book = models.DateTimeField(default=datetime.now())
    date_start = models.DateTimeField(default=datetime.now())
    tourer = models.ForeignKey(Tourer,on_delete=models.CASCADE)

    def __str__(self):
        return self.name_book + '-' + self.tourer.name

class Restaurant_tour(models.Model):
    book = models.ForeignKey(Book_Tour,on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    account = models.ForeignKey(Tourer,on_delete=models.CASCADE)
    date_book = models.DateTimeField(default=datetime.now())
    date_to = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.book.name_book + '-' + self.restaurant.name_restaurant

class Place_tour(models.Model):
    book = models.ForeignKey(Book_Tour,on_delete=models.CASCADE)
    place = models.ForeignKey(Place,on_delete=models.CASCADE)
    account = models.ForeignKey(Tourer,on_delete=models.CASCADE)
    date_book = models.DateTimeField(default=datetime.now())
    date_to = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.book.name_book + '-' + self.place.name_place

class Vehicle_tour(models.Model):
    book = models.ForeignKey(Book_Tour,on_delete=models.CASCADE)
    vehicle_details = models.ForeignKey(Vehicle_details,on_delete=models.CASCADE)
    account = models.ForeignKey(Tourer,on_delete=models.CASCADE)
    date_book = models.DateTimeField(default=datetime.now())
    date_to = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.book.name_book + '-' + self.vehicle.go_route

class House_tour(models.Model):
    book = models.ForeignKey(Book_Tour,on_delete=models.CASCADE)
    house = models.ForeignKey(House,on_delete=models.CASCADE)
    account = models.ForeignKey(Tourer,on_delete=models.CASCADE)
    date_book = models.DateTimeField(default=datetime.now())
    date_to = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.book.name_book + '-' + self.house.name_house


class Book_Tour_Details(models.Model):
    book = models.ForeignKey(Book_Tour,on_delete=models.CASCADE)
    place = models.ForeignKey(Place_tour,on_delete=models.CASCADE)
    house = models.ForeignKey(House_tour,on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant_tour,on_delete=models.CASCADE)
    vehicle= models.ForeignKey(Vehicle_tour,on_delete=models.CASCADE)

    def __str__(self):
        return self.book.name_book + '-' + self.place.place.name_place + '-' + self.house.house.name_house + '-' + self.restaurant.restaurant.name_restaurant + '-' + self.vehicle.vehicle_details.go_route

class Album_Tour(models.Model):
    book = models.ForeignKey(Book_Tour,on_delete=Book_Tour)
    img_album = models.FileField(upload_to = 'album/',default='/default/user-avatar-default-165.png')
    date_up = models.DateTimeField(default=datetime.now())
    place = models.ForeignKey(Place_tour,on_delete=models.CASCADE)