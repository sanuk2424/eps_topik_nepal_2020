from django.db import models


# Create your models here.
class Basic(models.Model):
    title = models.CharField(max_length=200, default="")
    content = models.TextField(default="")
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
