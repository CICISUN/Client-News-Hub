from django.db import models

# Create your models here.

class NewsFeeds(models.Model):
    title = models.CharField(max_length=300)
    keyword = models.CharField(max_length=100)
    date = models.DateField()
    source = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    url = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
