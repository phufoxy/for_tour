from django.urls import path, re_path
from . import views
import django.views.defaults
from django.conf.urls import handler404, handler500, url

urlpatterns = [
    path('places/',views.index,name='places'),
    path('places/<int:id>',views.places_details,name='places_details'),
    path('create_comment_place/<int:id>/',views.create_comment_place,name='create_comment_place'),
    path('IndexView_Place/',views.IndexView_Place.as_view(),name='IndexView_Place'),
    path('create_place_tour/<int:id>/',views.create_place_tour,name='create_place_tour'),


    # dashboard
    path('CreatePlace/',views.CreatePlace.as_view(),name='CreatePlace'),
    path('UpdatePlace/<int:pk>/',views.UpdatePlace.as_view(),name='UpdatePlace'),
    path('PlaceDelete/<int:pk>/delete/',views.PlaceDelete.as_view(),name='PlaceDelete'),
    path('IndexView_Place_City/',views.IndexView_Place_City.as_view(),name='IndexView_Place_City'),
    path('IndexView_Place_City/<int:pk>/',views.UpdatePlace_City.as_view(),name='UpdatePlace_City'),
    path('IndexView_Place_City/<int:pk>/delete/',views.PlaceDelete_City.as_view(),name='PlaceDelete_City'),
    path('IndexView_Place_details/',views.IndexView_Place_details.as_view(),name='IndexView_Place_details'),
    path('CreatePlaces_details/',views.CreatePlaces_details.as_view(),name='CreatePlaces_details'),
    path('CreatePlace_City/',views.CreatePlace_City.as_view(),name='CreatePlace_City'),
    path('IndexView_Place_City/<int:pk>/',views.UpdatePlaces_details.as_view(),name='UpdatePlaces_details'),
    path('IndexView_Place_City/<int:pk>/delete/',views.PlacesDelete_details.as_view(),name='PlacesDelete_details'),

]