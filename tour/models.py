from django.db import models
from datetime import datetime
from django.urls import reverse
from tourer.models import Tourer
# Create your models here.
    
class Tour(models.Model):
    TOUR_CHOICES = (
        ('Du Lịch Trong Nước','Du Lịch   Trong Nước'),
        ('Tour Nước Ngoài','Tour Nước Ngoài'),
    )
    CITY_CHOICES = (
        ('Miền Bắc',(
            ('Hà Nội','Hà Nội'),
            ('Sapa','Sapa')
        )),
        ('Miền Trung',(
            ('Đà Nẵng','Đà Nẵng'),
            ('Quảng Nam','Quảng Nam'),
            ('Quảng Ngãi','Quảng Ngãi'),
            ('Quy Nhơn','Quy Nhơn'),
            ('Nha Trang','Nha Trang'),
        )),
        ('Miền Nam',(
            ('Sài Gòn','Sài Gòn'),
            ('Sài Gòn','Sài Gòn')
        ))
    )
    name_tour = models.CharField(max_length = 250)
    person = models.FloatField(default=1)
    image_tour = models.FileField(upload_to = 'tour/',default='/default/user-avatar-default-165.png')
    date_tour = models.FloatField(default=1)
    type_tour = models.CharField(max_length=250,choices=TOUR_CHOICES,null=True,blank=True,default='Du Lịch Trong Nước')
    city = models.CharField(max_length=250,choices=CITY_CHOICES,null=True,blank=True,default='Đà Nẵng')

    def __str__(self):
        return self.name_tour + ' -- ' + str(self.date_tour) + ' Ngày'

    def get_absolute_url(self):
        return reverse('ListTour')

    class Meta:
        ordering = ["-id"]

class PlaceTour(models.Model):
    tour = models.ForeignKey(Tour,on_delete=models.CASCADE)
    name_place = models.CharField(max_length=250)
    price = models.FloatField(default=0)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    image_place = models.FileField(upload_to='tour/',default='/default/user-avatar-default-165.png')
   
    def __str__(self):
        return self.tour.name_tour + ' -- ' + str(self.price) + ' VNĐ'

    def get_absolute_url(self):
        return reverse('ListPlaceTour')

    class Meta:
        ordering = ["-id"]

class BookTour(models.Model):
    accout = models.ForeignKey(Tourer,on_delete=models.CASCADE)
    date_book = models.DateTimeField(default=datetime.now())
    date_start = models.DateTimeField(default=datetime.now())
    tour = models.ForeignKey(Tour,on_delete=models.CASCADE)

    class Meta:
        ordering = ['date_start']

    def __str__(self):
        return self.accout.email + ' -- ' + self.tour.name_tour


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
 
    class Meta:
        abstract = True
 
class Student(CommonInfo):
    home_group = models.CharField(max_length=5)