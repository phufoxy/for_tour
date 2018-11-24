from django.db import models
from datetime import datetime
from django.urls import reverse

# Create your models here.
class Tour(models.Model):
    TOUR_CHOICES = (
        ('Du Lịch Trong Nước','Du Lịch   Trong Nước'),
        ('Tour Nước Ngoài','Tour Nước Ngoài'),
    )
    name_tour = models.CharField(max_length = 250)
    person = models.FloatField(default=1)
    image_tour = models.FileField(upload_to = 'tour/',default='/default/user-avatar-default-165.png')
    date_tour = models.FloatField(default=1)
    type_tour = models.CharField(max_length=250,choices=TOUR_CHOICES,null=True,blank=True,default='Du Lịch Trong Nước')
    price = models.FloatField(default=0)


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
        return self.tour + ' -- ' + str(self.price) + ' VNĐ'

    def get_absolute_url(self):
        return reverse('ListPlaceTour')

    class Meta:
        ordering = ["-id"]

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
 
    class Meta:
        abstract = True
 
class Student(CommonInfo):
    home_group = models.CharField(max_length=5)