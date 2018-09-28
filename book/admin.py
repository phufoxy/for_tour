from django.contrib import admin
from .models import Book_Tour,Restaurant_tour,Place_tour,Vehicle_tour,House_tour,Book_Tour_Details,Album_Tour
# Register your models here.
admin.site.register(Book_Tour)
admin.site.register(Restaurant_tour)
admin.site.register(Place_tour)
admin.site.register(Vehicle_tour)
admin.site.register(House_tour)
admin.site.register(Book_Tour_Details)
admin.site.register(Album_Tour)