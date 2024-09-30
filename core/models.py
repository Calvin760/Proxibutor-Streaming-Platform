from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()

class Artist(models.Model):
    stage_name = models.CharField(max_length=255)
    header_image = models.ImageField(upload_to='artist_headers/')
    profile_picture = models.ImageField(upload_to='artist_profiles/')
    bio = models.TextField()

    def __str__(self):
        return self.stage_name

class Music(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=255, verbose_name="Song Title")
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True)  # Making artist nullable
    featured_artists = models.CharField(max_length=255, blank=True, null=True, verbose_name="Featured Artists")
    release_date = models.DateField(verbose_name="Release Date")
    cover_art = models.ImageField(upload_to='release_images/', verbose_name="Cover Art", blank=True, null=True)
    song = models.FileField(upload_to='release_songs/', verbose_name="Song File", blank=True, null=True)
    credits = models.TextField(blank=True, null=True, verbose_name="Credits") 
    genre = models.CharField(max_length=50, blank=True, null=True, verbose_name="Genre")

    class Meta:
        ordering = ['release_date']
        verbose_name = "Music Release"
        verbose_name_plural = "Music Releases"
        unique_together = ('title', 'artist')  # Ensure title and artist combo is unique

    def __str__(self):
        return f"{self.title} by {self.artist.stage_name if self.artist else 'Unknown Artist'}"

    def get_featured_artists_list(self):
        return self.featured_artists.split(',') if self.featured_artists else []
