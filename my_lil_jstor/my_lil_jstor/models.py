from django.db import models


class ColoringBook(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')