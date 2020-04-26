from django.contrib import admin

# Register your models here.
from book.models import Book
from book.models import AudioMp3File

admin.site.register(Book)
admin.site.register(AudioMp3File)
