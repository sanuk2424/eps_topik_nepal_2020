from django.conf.urls import url
from django.urls import path

from book import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('book_detail/<int:myid>', views.book_detail, name='BookDetail'),
    path('pdf_view/<str:file>', views.pdf_view, name='PdfView'),



    # path('pdf_view', views.pdf_view, name='PdfView'),



]
