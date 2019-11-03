from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from movie_details.models import movie_details
from filmstars.models import filmstars
from datetime import datetime
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class latest_news(models.Model):
    news_id = models.IntegerField(primary_key=True,default="",validators = [MinValueValidator(0)])
    actor_id = models.ForeignKey(filmstars,on_delete=models.CASCADE)
    movie_id = models.ForeignKey(movie_details, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE , default = '')
    news_message = models.TextField()
    title = models.CharField(max_length=200)
    news_dt = models.DateTimeField(default=timezone.now())
    news_image = models.ImageField(blank = True , null = True)

    def approve_comments(self):
        return self.comments.filter(approve_comments=True)

    def __str__(self):
        return self.title


class news_comment(models.Model):
    post = models.ForeignKey('latest_news.latest_news',related_name = 'comments', on_delete=models.CASCADE)
    author = models.CharField(max_length = 200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comments = models.BooleanField(default = False)
