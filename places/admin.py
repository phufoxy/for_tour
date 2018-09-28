from django.contrib import admin
from .models import City,Place,Place_details,Comment_place
# Register your models here.
admin.site.register(City)
admin.site.register(Place)
admin.site.register(Place_details)
admin.site.register(Comment_place)
