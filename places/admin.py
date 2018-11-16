from django.contrib import admin
from .models import Place,Place_details,Comment_place,Email
# Register your models here.
admin.site.register(Place)
admin.site.register(Place_details)
admin.site.register(Comment_place)
admin.site.register(Email)
