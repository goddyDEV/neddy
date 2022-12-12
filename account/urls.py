from django.urls import path
from . import views

app_name = 'account'


urlpatterns = [

    path('login/',views.auth_login, name='login'),
    path('logout/',views.auth_logout, name='logout'),
    path('user-profile/',views. change_password, name='user-profile'),
    
]