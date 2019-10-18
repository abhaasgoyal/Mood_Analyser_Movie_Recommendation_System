from django.db import models
from dateutil.relativedelta import relativedelta
from django.core.validators import MaxValueValidator, MinValueValidator


class login_credentials(models.Model):
    user_id = models.IntegerField(primary_key=True,validators = [MinValueValidator(0)])
    email = models.CharField(max_length=15)
    password = models.CharField(max_length=15)

class users(models.Model):
    user_id = models.ForeignKey(login_credentials,on_delete=models.CASCADE)
    username = models.CharField(primary_key=True,max_length=15)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=1)
    nationality = models.CharField(max_length=30)
    date_of_birth = models.DateField(max_length=8)
    age = models.IntegerField()
    def __str__(self):
        today = date.today()
        delta = relativedelta(today, self.dob)
        return str(delta.years)

    profile_picture = models.CharField(max_length=30)
    about_user = models.TextField(max_length=30)
