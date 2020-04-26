from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200, default="")
    content = models.TextField(default="")

    pdf_file = models.FileField(upload_to='book/pdf', default='')
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class AudioMp3File(models.Model):
    book_chapter = models.ForeignKey(Book, on_delete=models.CASCADE)

    mp3_file = models.FileField(upload_to='book/mp3', default='')
    created_date = models.DateTimeField(auto_now=True)
