from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=300)

class Addressbook(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
 
class Playlist(models.Model):
    Playlist_name = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)
    Song_name = models.CharField(max_length=100)
    Singer_name = models.CharField(max_length=100)

class Arijit_Song(models.Model):
    song_name = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='documents')
    song =models.FileField(upload_to='documents')
   
    def __str__(self):
        return self.song_name