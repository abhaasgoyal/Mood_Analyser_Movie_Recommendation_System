from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from movie_details.models import movie_details
from filmstars.models import filmstars
from datetime import datetime
# Create your models here.

class latest_news(models.Model):
    news_id = models.IntegerField(primary_key=True,default="",validators = [MinValueValidator(0)])
    actor_id = models.ForeignKey(filmstars,on_delete=models.CASCADE)
    movie_id = models.ForeignKey(movie_details, on_delete=models.CASCADE)
    news_message = models.TextField(max_length=255)
    title = models.TextField(max_length=30)
    news_dt = models.DateTimeField()
