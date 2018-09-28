from django.urls import path, re_path
from . import views
import django.views.defaults
from django.conf.urls import handler404, handler500, url

urlpatterns = [
    path('book/',views.book,name='book'),
    path('book_details/',views.book_details,name='book_details'),
    path('create_book/',views.create_book,name='create_book'),
    path('delete_book/<int:id>/',views.delete_book,name='delete_book'),
    path('book_details/<int:id>/',views.book_details_to,name='book_details_to')
]