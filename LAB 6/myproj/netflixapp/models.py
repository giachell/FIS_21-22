from django.db import models

# Create your models here.


class Movie(models.Model):
    """A data structure for Netflix movies and series"""
    title = models.CharField(max_length=1000, blank=False)
    type = models.CharField(max_length=1000, blank=False)
    description = models.CharField(max_length=1000, blank=True)
    director = models.CharField(max_length=1000, blank=True)
    country = models.CharField(max_length=1000, blank=True)
    cast = models.CharField(max_length=1000, blank=True)
    date_added = models.DateField(blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    rating = models.CharField(max_length=1000, blank=True)
    duration = models.CharField(max_length=1000, blank=True)
    listed_in = models.CharField(max_length=1000, blank=True)