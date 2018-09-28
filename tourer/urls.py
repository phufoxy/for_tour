from django.urls import path
from . import views
urlpatterns = [
    path('',views.login,name='login'),
    path('login_form/',views.login_form,name='login_form'),
    path('register/',views.Register.as_view(),name='Register'),
    path('logout/',views.logout,name='logout'),
]