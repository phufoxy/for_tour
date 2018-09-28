from django.contrib import admin
from .models import Type_vehicle,City,Vehicle,Vehicle_details,Car_details,Comment_Vehicle
# Register your models here.
admin.site.register(Type_vehicle)
admin.site.register(Vehicle)
admin.site.register(City)
admin.site.register(Vehicle_details)
admin.site.register(Car_details)
admin.site.register(Comment_Vehicle)
# admin.site.register(Vehicle_Tour)