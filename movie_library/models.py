from django.db import models
from movie_details.models import movie_details
from user_details.models import User_Profile_Info
from django.core.validators import MaxValueValidator, MinValueValidator

class movie_library(models.Model):
    movie_id = models.ForeignKey(movie_details,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User_Profile_Info, on_delete=models.CASCADE)
    your_rating = models.IntegerField(validators = [MinValueValidator(0),MaxValueValidator(10)])
    status = models.CharField(max_length=1)
    progress = models.IntegerField(validators = [MinValueValidator(0)])
