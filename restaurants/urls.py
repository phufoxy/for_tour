from django.urls import path, re_path
from . import views
import django.views.defaults
from django.conf.urls import handler404, handler500, url

urlpatterns = [
    path('restaurant/',views.index,name='restaurant'),
    path('restaurant/<int:id>/',views.eating,name='eating'),
    path('create_comment_eating/<int:id>/',views.create_comment_eating,name='create_comment_eating'),
    path('restaurant/<int:id>/eating/<int:id_restaurant>/',views.eating_details,name='eating_details'),
    # city
    path('IndexView_Restaurants_City/',views.IndexView_Restaurants_City.as_view(),name='IndexView_Restaurants_City'),
    path('CreateRestaurants_City/',views.CreateRestaurants_City.as_view(),name='CreateRestaurants_City'),
    path('IndexView_Restaurants_City/<int:pk>/',views.UpdateRestaurants_City.as_view(),name='UpdateRestaurants_City'),
    path('IndexView_Restaurants_City/<int:pk>/delete/',views.RestaurantsDelete_City.as_view(),name='RestaurantsDelete_City'),
    # restaurants
    path('IndexView_Restaurants/',views.IndexView_Restaurants.as_view(),name='IndexView_Restaurants'),
    path('CreateRestaurant/',views.CreateRestaurant.as_view(),name='CreateRestaurant'),
    path('IndexView_Restaurants/<int:pk>/',views.UpdateRestaurant.as_view(),name='UpdateRestaurant'),
    path('IndexView_Restaurants/<int:pk>/delete/',views.RestaurantDelete.as_view(),name='RestaurantDelete'),
    # eating
    path('IndexView_Eating/',views.IndexView_Eating.as_view(),name='IndexView_Eating'),
    path('CreateEating/',views.CreateEating.as_view(),name='CreateEating'),
    path('IndexView_Eating/<int:pk>/',views.UpdateEating.as_view(),name='UpdateEating'),
    path('IndexView_Eating/<int:pk>/delete/',views.EatingDelete.as_view(),name='EatingDelete'),
    # eating_details
    path('IndexView_Eating_details/',views.IndexView_Eating_details.as_view(),name='IndexView_Eating_details'),
    path('CreateEating_details/',views.CreateEating_details.as_view(),name='CreateEating_details'),
    path('IndexView_Eating_details/<int:pk>/',views.UpdateEating_details.as_view(),name='UpdateEating_details'),
    path('IndexView_Eating_details/<int:pk>/delete/',views.Eating_detailsDelete.as_view(),name='Eating_detailsDelete'),
  
]