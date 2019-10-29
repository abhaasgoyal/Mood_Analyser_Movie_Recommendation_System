from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class movie_details(models.Model):
    movie_id = models.IntegerField(primary_key=True,validators = [MinValueValidator(0)])
    movie_name = models.CharField(max_length=30)
    imdb_rating = models.IntegerField(validators = [MinValueValidator(0),MaxValueValidator(10)])
    rt_rating = models.IntegerField(validators = [MinValueValidator(0),MaxValueValidator(100)])
    metacritic_rating = models.IntegerField(validators = [MinValueValidator(0),MaxValueValidator(100)])
    movie_image = models.ImageField(default='')
    genre = models.CharField(max_length=30)
    release_date = models.DateField()
    total_episodes = models.IntegerField(validators = [MinValueValidator(0)])
    synopsis = models.TextField(max_length=30)
