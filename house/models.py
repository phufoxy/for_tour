from django.db import models
from datetime import datetime
from tourer.models import Tourer
from django.urls import reverse

# Create your models here.

class House(models.Model):
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
    TYPE_CHOICES = (
        ('Nhà Nghĩ','Nhà Nghĩ'),
        ('Khách Sạn','Khách Sạn'),
        ('Nhà Trọ','Nhà Trọ'),
        ('HomeStay','HomeStay'),
    )
    ROOM_CHOICES = (
        ('Đơn','Đơn'),
        ('Đôi','Đôi'),
        ('Ba','Ba'),
    )
    name_house = models.CharField(max_length=250)
    city = models.CharField(max_length=250,choices=CITY_CHOICES,null=True,blank=True,default='Đà Nẵng')
    address = models.CharField(max_length=250,null=True,blank=True)
    type_house = models.CharField(max_length=250,choices=TYPE_CHOICES,default='Nhà Nghĩ')
    image_house = models.FileField(upload_to = 'house/',default='/default/user-avatar-default-165.png')
    review = models.IntegerField(default=0)
    star = models.FloatField(default=0)
    room_type = models.CharField(max_length=250,null=True,blank=True,choices=ROOM_CHOICES,default='Đơn')
    price = models.FloatField(default=0,null=True,blank=True)

    def get_absolute_url(self):
        return reverse('ListHouse')


    def __str__(self):
        return self.name_house + '-' + self.city

class House_details(models.Model):
    house = models.ForeignKey(House,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    start_status = models.CharField(max_length=5000)
    end_status = models.CharField(max_length=5000)
    img_status = models.FileField(upload_to='house/book/',default='/default/user-avatar-default-165.png')

    def get_absolute_url(self):
        return reverse('ListHouseDetails')

    def __str__(self):
        return self.house + '-' + self.title

class Comment_house(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    commnet = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now())
    account = models.ForeignKey(Tourer,on_delete=models.CASCADE)
