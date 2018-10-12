from django.urls import path, re_path
from . import views
import django.views.defaults
from django.conf.urls import handler404, handler500, url

urlpatterns = [
    path('house/',views.house,name='house'),
    path('house/<int:id>/',views.house_details,name='house_details'),
    path('dashboard/',views.dashboard_home,name='dashboard_home'),
    path('dashboard/house/',views.IndexView_House.as_view(),name='IndexView_House'),
    path('dashboard/createhouse/',views.CreateHouse.as_view(),name='CreateHouse'),
    path('create_comment_house/<int:id>/',views.create_comment_house,name='create_comment_house'),
    path('create_house_tour/<int:id>/',views.create_house_tour,name='create_house_tour'),
    path('dashboard/house/<int:pk>/delete/',views.HouseDelete.as_view(),name='house-delete'),
    path('dashboard/house/<int:pk>/',views.UpdateHouse.as_view(),name='house-update'),
    # House details
    path('dashboard/house_details/',views.IndexView_House_details.as_view(),name='IndexView_House_details'),
    path('dashboard/create_house_details/',views.CreateHouse_details.as_view(),name='CreateHouse_details'),
    path('dashboard/house_details/<int:pk>/delete/',views.HouseDelete_details.as_view(),name='HouseDelete_details'),
    path('dashboard/house_details/<int:pk>/',views.UpdateHouse_details.as_view(),name='UpdateHouse_details'),
    # house city
    path('dashboard/house_city/',views.IndexView_House_City.as_view(),name='IndexView_House_City'),
    path('dashboard/create_house_city/',views.CreateHouse_City.as_view(),name='CreateHouse_City'),
    path('dashboard/house_city/<int:pk>',views.UpdateHouse_City.as_view(),name='UpdateHouse_City'),
    path('dashboard/house_city/<int:pk>/delete/',views.HouseDelete_City.as_view(),name='HouseDelete_City'),

]