from django.db import models
from datetime import datetime    
from django.urls import reverse
# from django.forms import CharField, Form, PasswordInput
# Create your models here.
class Tourer(models.Model):
    email = models.CharField(max_length=250,null=True,blank=True)
    name = models.CharField(max_length = 250)
    avatar = models.FileField(upload_to = 'tourer/',default='/default/user-avatar-default-165.png')
    password = models.CharField(max_length=250)
    question = models.CharField(max_length=250,default='question')


    def get_absolute_url(self):
        return reverse('house')

    def __str__(self):
        return self.name