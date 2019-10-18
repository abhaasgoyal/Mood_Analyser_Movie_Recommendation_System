from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from movie_details.models import movie_details
from filmstars.models import filmstars

class movie_and_actors(models.Model):
    actor_id = models.ForeignKey(actor_id,on_delete=models.CASCADE)
