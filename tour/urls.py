from django.urls import path,include
from . import views
urlpatterns = [
    # dashboard
    path('dashboard/tour/',include([
        # tour
        path('',views.ListTour.as_view(),name='ListTour'),
        path('create/',views.AddTour.as_view(),name='AddTour'),
        path('<int:pk>/delete/',views.DeleteTour.as_view(),name='DeleteTour'),
        path('<int:pk>/',views.UpdateTour.as_view(),name='UpdateTour'),
        path('read/<int:pk>/',views.TourReadView.as_view(),name='TourReadView'),
        path('place/',include([
            path('',views.ListPlaceTour.as_view(),name='ListPlaceTour'),
            path('create/',views.AddPlaceTour.as_view(),name='AddPlaceTour'),
            path('<int:pk>/',views.UpdatePlaceTour.as_view(),name='UpdatePlaceTour'),
            path('<int:pk>/delete/',views.DeletePlaceTour.as_view(),name='DeletePlaceTour'),
            path('read/<int:pk>/',views.PlaceTourReadView.as_view(),name='PlaceTourReadView'),
        ]))
    ])),
    # home
    path('tour/',include([
        path('',views.list_tour,name='list_tour'),
        path('<int:id>/',views.tour_details,name='tour_details'),
        path('add/<int:id>/',views.add_tour,name='add_tour'),
        path('search/<str:name>/',views.search_tour_place,name='search_tour_place'),
        path('search/',views.search_form,name='search_tour'),
        path('search/<str:city>/<str:price>/<str:person>/<str:date>/',views.search_tour_place_price,name='search_tour_place_price'),
    ]))
]