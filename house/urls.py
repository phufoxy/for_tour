from django.urls import path, re_path
from . import views
import django.views.defaults
from django.conf.urls import handler404, handler500, url

urlpatterns = [
    path('house/',views.house,name='house'),
    path('house/<int:id>/',views.house_details,name='house_details'),
    path('dashboard/',views.dashboard_home,name='dashboard_home'),
    path('IndexView_House/',views.IndexView_House.as_view(),name='IndexView_House'),
    path('CreateHouse/',views.CreateHouse.as_view(),name='CreateHouse'),
    path('create_comment_house/<int:id>/',views.create_comment_house,name='create_comment_house'),
    path('IndexView_House/<int:pk>/delete/',views.HouseDelete.as_view(),name='house-delete'),
    path('IndexView_House/<int:pk>/',views.UpdateHouse.as_view(),name='house-update'),
    path('IndexView_House_details/',views.IndexView_House_details.as_view(),name='IndexView_House_details'),
    path('CreateHouse_details/',views.CreateHouse_details.as_view(),name='CreateHouse_details'),
    path('IndexView_House_details/<int:pk>/delete/',views.HouseDelete_details.as_view(),name='HouseDelete_details'),
    path('IndexView_House_details/<int:pk>/',views.UpdateHouse_details.as_view(),name='UpdateHouse_details'),
    path('IndexView_House_City/',views.IndexView_House_City.as_view(),name='IndexView_House_City'),
    path('CreateHouse_City/',views.CreateHouse_City.as_view(),name='CreateHouse_City'),
    path('IndexView_House_City/<int:pk>',views.UpdateHouse_City.as_view(),name='UpdateHouse_City'),
    path('IndexView_House_City/<int:pk>/delete/',views.HouseDelete_City.as_view(),name='HouseDelete_City'),

]