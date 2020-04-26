from django.conf.urls import url
from django.urls import path

from verb import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('verb_detail/<int:myid>', views.verb_detail, name='VerbDetail'),

]
