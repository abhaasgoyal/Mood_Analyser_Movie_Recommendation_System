from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from movie_details.models import movie_details
from user_details.models import User_Profile_Info
from datetime import datetime
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title= models.CharField(max_length=255, unique=True)
    content= models.TextField()


class forum_posts(models.Model):
    movie_id = models.ForeignKey(movie_details, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User_Profile_Info, on_delete=models.CASCADE)
    post_id = models.IntegerField(primary_key=True,default="",validators = [MinValueValidator(0)])
    post_message = models.TextField(max_length=255)
    title = models.TextField(max_length=30)
    images = models.ImageField()

    def publish(self):
        self.news_dt = timezone.now()
        self.save()

class comments(models.Model):
    comment_id = models.IntegerField(primary_key=True,default="",validators = [MinValueValidator(0)])
    post_id = models.ForeignKey(forum_posts, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User_Profile_Info, on_delete=models.CASCADE)
    comment_message = models.TextField(max_length=255)
    comment_dt = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.comment_dt = timezone.now()
        self.save()

class replies(models.Model):
    reply_id = models.IntegerField(primary_key=True,default="",validators = [MinValueValidator(0)])
    comment_id = models.ForeignKey(forum_posts, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User_Profile_Info, on_delete=models.CASCADE)
    reply_message = models.TextField(max_length=255)
    reply_dt = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.reply_dt = timezone.now()
        self.save()
