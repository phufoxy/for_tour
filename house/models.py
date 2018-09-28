from django.db import models
from datetime import datetime
from tourer.models import Tourer
from django.urls import reverse

# Create your models here.
class City(models.Model):
    city = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('IndexView_House_City')

    def __str__(self):
        return self.city + '-' + self.address

# class Room(models.Model):
    # house = models.ForeignKey(House,on_delete=models.CASCADE)
    # room_type = models.CharField(max_length=250)
    # price = models.FloatField(default=0)

class House(models.Model):
    name_house = models.CharField(max_length=250)
    location = models.ForeignKey(City,on_delete=models.CASCADE)
    type_house = models.CharField(max_length=250)
    image_house = models.FileField(upload_to = 'house/',default='/default/user-avatar-default-165.png')
    review = models.IntegerField(default=0)
    star = models.FloatField(default=0)
    room_type = models.CharField(max_length=250,null=True,blank=True)
    price = models.FloatField(default=0,null=True,blank=True)

    def get_absolute_url(self):
        return reverse('IndexView_House')


    def __str__(self):
        return self.name_house + '-' + self.location.city

class House_details(models.Model):
    house = models.ForeignKey(House,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    start_status = models.CharField(max_length=5000)
    end_status = models.CharField(max_length=5000)
    img_status = models.FileField(upload_to='house/book/',default='/default/user-avatar-default-165.png')

    def get_absolute_url(self):
        return reverse('IndexView_House_details')

    def __str__(self):
        return self.house + '-' + self.title

class Comment_house(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    commnet = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now())
    account = models.ForeignKey(Tourer,on_delete=models.CASCADE)

# class House_tour(models.Model):
#     house = models.ForeignKey(House,on_delete=models.CASCADE)
#     account = models.ForeignKey(Tourer,on_delete=models.CASCADE)
#     date = models.DateTimeField(default=datetime.now())
