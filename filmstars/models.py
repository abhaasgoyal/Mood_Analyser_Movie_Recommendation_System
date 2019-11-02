from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class filmstars(models.Model):
    name = models.CharField(max_length = 10)
    movie_id = models.IntegerField(primary_key=True,validators = [MinValueValidator(0)])
    date_of_birth = models.DateField(max_length=8)
    @property
    def age(self):
        today = date.today()
        delta = relativedelta(today, self.date_of_birth)
        return str(delta.years)
    died = models.DateField(max_length=8)
    sex = models.CharField(max_length=1)
    years_active = models.IntegerField()
    actor_image = models.ImageField()
    synopsis = models.TextField(max_length=30)
