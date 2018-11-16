from django.db import models
from datetime import datetime
from tourer.models import Tourer
from django.urls import reverse
# Create your models here.
class Place(models.Model):
    TYPE_PLACE = (
        ('Cầu','Cầu'),
        ('Sông','Sông'),
        ('Hồ','Hồ'),
        ('Núi','Núi'),
        ('Biển','Biển')
    )
    CITY_CHOICES = (
        ('Đà Nẵng','Đà Nẵng'),
        ('Hà Nội','Hà Nội'),
        ('Hồ Chí Minh','Hồ Chí Minh'),
        ('Đà Lạt','Đà Lạt'),
        ('Nha Trang','Nha Trang'),
        ('Quảng Nam','Quảng Nam'),
        ('Quảng Ngãi','Quảng Ngãi'),
        ('Huế','Huế'),
        ('Gia Lai','Gia Lai'),
        ('Ninh Bình','Ninh Bình'),
        ('Quy Nhơn','Quy Nhơn'),
    )
    name_place = models.CharField(max_length=250)
    city = models.CharField(max_length=250,null=True,blank=True,choices=CITY_CHOICES,default='Đà Nẵng')
    address = models.CharField(max_length=250,null=True,blank=True)
    type_place = models.CharField(max_length=250)
    image_place = models.FileField(upload_to = 'place/',default='/default/user-avatar-default-165.png')
    review = models.IntegerField(default=0)
    star = models.FloatField(default=0)
    price = models.FloatField(default=0,null=True,blank=True)

    def get_absolute_url(self):
        return reverse('ListPlace')

    def __str__(self):
        return self.name_place + '-' + self.city

class Place_details(models.Model):
    place = models.ForeignKey(Place,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    start_status = models.CharField(max_length=5000)
    end_status = models.CharField(max_length=5000)
    img_status = models.FileField(upload_to='place/book/',default='/default/user-avatar-default-165.png')

    def get_absolute_url(self):
        return reverse('ListPlaceDetails')

    def __str__(self):
        return self.place.name_place + '-' + self.title

class Comment_place(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    commnet = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now())
    account = models.ForeignKey(Tourer,on_delete=models.CASCADE)


class Email(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)