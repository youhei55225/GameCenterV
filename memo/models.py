from django.db import models

# Create your models here.

class Memo(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.CharField(max_length=255)
    my_char = models.CharField(max_length=255)
    opp_char = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)
    date_time = models.DateTimeField(auto_now=True)
