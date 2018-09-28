from django.db import models
from datetime import datetime
from tourer.models import Tourer
from django.urls import reverse
# Create your models here.
class City(models.Model):
    city = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('IndexView_Place_City')

    def __str__(self):
        return self.city + '-' + self.address


class Place(models.Model):
    name_place = models.CharField(max_length=250)
    location = models.ForeignKey(City,on_delete=models.CASCADE)
    type_place = models.CharField(max_length=250)
    image_place = models.FileField(upload_to = 'place/',default='/default/user-avatar-default-165.png')
    review = models.IntegerField(default=0)
    star = models.FloatField(default=0)
    price = models.FloatField(default=0,null=True,blank=True)

    def get_absolute_url(self):
        return reverse('IndexView_Place')

    def __str__(self):
        return self.name_place + '-' + self.location.city

class Place_details(models.Model):
    place = models.ForeignKey(Place,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    start_status = models.CharField(max_length=5000)
    end_status = models.CharField(max_length=5000)
    img_status = models.FileField(upload_to='place/book/',default='/default/user-avatar-default-165.png')

    def get_absolute_url(self):
        return reverse('IndexView_Place_details')

    def __str__(self):
        return self.place + '-' + self.title

class Comment_place(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    commnet = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now())
    account = models.ForeignKey(Tourer,on_delete=models.CASCADE)

