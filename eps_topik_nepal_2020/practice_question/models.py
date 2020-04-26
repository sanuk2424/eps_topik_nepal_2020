from django.db import models


# Create your models here.
class ImageTypeQuestion(models.Model):
    content = models.TextField(default='')
    image = models.ImageField(upload_to='practice_question/images', default='')
    option1 = models.CharField(max_length=100, default='')
    option2 = models.CharField(max_length=100, default='')
    option3 = models.CharField(max_length=100, default='')
    option4 = models.CharField(max_length=100, default='')
    answer = models.CharField(max_length=100, default='')
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


class FillingTypeQuestion(models.Model):
    content = models.TextField(default='')
    option1 = models.CharField(max_length=100, default='')
    option2 = models.CharField(max_length=100, default='')
    option3 = models.CharField(max_length=100, default='')
    option4 = models.CharField(max_length=100, default='')
    answer = models.CharField(max_length=100, default='')
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


class PassageTypeQuestion(models.Model):
    content = models.TextField(default='')
    option1 = models.CharField(max_length=100, default='')
    option2 = models.CharField(max_length=100, default='')
    option3 = models.CharField(max_length=100, default='')
    option4 = models.CharField(max_length=100, default='')
    answer = models.CharField(max_length=100, default='')
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
