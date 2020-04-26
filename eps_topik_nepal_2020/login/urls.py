from django.conf.urls import url
from django.urls import path

from login import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('signup', views.signup, name='SignUp'),
    path('signin', views.signin, name='SignUp'),
    path('logout', views.logout, name='SignUp'),

]
