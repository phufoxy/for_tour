from django.urls import path, re_path
from . import views
import django.views.defaults
from django.conf.urls import handler404, handler500, url

urlpatterns = [
    path('vehicle/',views.index,name='vehicle'),
    path('vehicle/<int:id>/',views.vehicle_details,name='vehicle_details'),
    path('vehicle/<int:id>/car/<int:id_car>/',views.car_details,name='car_details'),
    path('create_comment_vehicle/<int:id>/',views.create_comment_vehicle,name='create_comment_vehicle'),
    path('create_vehicle_tour/<int:id>/',views.create_vehicle_tour,name='create_vehicle_tour'),
     # city
    path('IndexView_Vehicle_City/',views.IndexView_Vehicle_City.as_view(),name='IndexView_Vehicle_City'),
    path('CreateVehicle_City/',views.CreateVehicle_City.as_view(),name='CreateVehicle_City'),
    path('IndexView_Vehicle_City/<int:pk>/',views.UpdateVehicle_City.as_view(),name='UpdateVehicle_City'),
    path('IndexView_Vehicle_City/<int:pk>/delete/',views.VehicleDelete_City.as_view(),name='VehicleDelete_City'),
       # Type_vehicle
    path('IndexView_Type_vehicle/',views.IndexView_Type_vehicle.as_view(),name='IndexView_Type_vehicle'),
    path('CreateType_vehicle/',views.CreateType_vehicle.as_view(),name='CreateType_vehicle'),
    path('IndexView_Type_vehicle/<int:pk>/',views.UpdateType_vehicle.as_view(),name='UpdateType_vehicle'),
    path('IndexView_Type_vehicle/<int:pk>/delete/',views.Type_vehicleDelete.as_view(),name='Type_vehicleDelete'),
      # vehicle
    path('IndexView_vehicle/',views.IndexView_vehicle.as_view(),name='IndexView_vehicle'),
    path('Create_Vehicle/',views.Create_Vehicle.as_view(),name='Create_Vehicle'),
    path('IndexView_vehicle/<int:pk>/',views.UpdateVehicle.as_view(),name='UpdateVehicle'),
    path('IndexView_vehicle/<int:pk>/delete/',views.VehicleDelete.as_view(),name='VehicleDelete'),
      # vehicle-details
    path('IndexView_vehicle_details/',views.IndexView_vehicle_details.as_view(),name='IndexView_vehicle_details'),
    path('Create_vehicle_details/',views.Create_vehicle_details.as_view(),name='Create_vehicle_details'),
    path('IndexView_vehicle_details/<int:pk>/',views.Updatevehicle_details.as_view(),name='Updatevehicle_details'),
    path('IndexView_vehicle_details/<int:pk>/delete/',views.Vehicle_detailsDelete.as_view(),name='Vehicle_detailsDelete'),
    
       # car
    path('IndexView_car/',views.IndexView_car.as_view(),name='IndexView_car'),
    path('Create_Car/',views.Create_Car.as_view(),name='Create_Car'),
    path('IndexView_car/<int:pk>/',views.UpdateCar.as_view(),name='UpdateCar'),
    path('IndexView_car/<int:pk>/delete/',views.Vehicle_detailsDelete.as_view(),name='Vehicle_detailsDelete'),
    
]