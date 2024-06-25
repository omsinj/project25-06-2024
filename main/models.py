# main/models.py
from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

class Resource(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    description = models.TextField()

class CulturalJourney(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_url = models.URLField()

class Developer(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
