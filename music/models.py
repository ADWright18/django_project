from django.db import models

# Create your models here.

class Album(models.Model):
    album_name = models.CharField(max_length=200)
    album_date = models.DateTimeField('date released')

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=200)
