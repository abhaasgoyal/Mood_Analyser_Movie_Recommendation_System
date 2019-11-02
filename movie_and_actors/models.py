from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from movie_details.models import movie_details
from filmstars.models import filmstars
from latest_news.models import latest_news

class movie_and_actors(models.Model):
    actor_id = models.ForeignKey(filmstars,on_delete=models.CASCADE)
    movie_id = models.ForeignKey(movie_details, on_delete=models.CASCADE)

class news_and_actors(models.Model):
    actor_id = models.ForeignKey(filmstars,on_delete=models.CASCADE)
    news_id = models.ForeignKey(latest_news,on_delete=models.CASCADE)
