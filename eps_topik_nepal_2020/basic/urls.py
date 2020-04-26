from django.conf.urls import url
from django.urls import path

from basic import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('basic_detail/<int:myid>', views.basic_detail, name='BasicDetail'),

]
