from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.login,name='login'),
    path('login_form/',views.login_form,name='login_form'),
    path('register/',views.register_main,name='Register'),
    path('logout/',views.logout,name='logout'),
    path('signup/',views.form_signup,name='signup'),
]