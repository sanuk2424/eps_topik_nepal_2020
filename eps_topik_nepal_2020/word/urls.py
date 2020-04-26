from django.conf.urls import url
from django.urls import path

from word import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('word_detail/<int:myid>', views.word_detail, name='WordDetail'),
    path('pdf',views.getpdf)

]
