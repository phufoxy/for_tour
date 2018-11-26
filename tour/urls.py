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
        path('place/',include([
            path('',views.ListPlaceTour.as_view(),name='ListPlaceTour'),
            path('create/',views.AddPlaceTour.as_view(),name='AddPlaceTour'),
            path('<int:pk>/',views.UpdatePlaceTour.as_view(),name='UpdatePlaceTour'),
            path('<int:pk>/delete/',views.DeletePlaceTour.as_view(),name='DeletePlaceTour'),
        ]))
    ])),
    # home
    path('tour/',include([
        path('',views.list_tour,name='list_tour'),
        path('<int:id>/',views.tour_details,name='tour_details'),
        path('add/<int:id>/',views.add_tour,name='add_tour')
    ]))
]