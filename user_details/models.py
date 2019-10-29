from django.db import models
from dateutil.relativedelta import relativedelta
from django.core.validators import MaxValueValidator, MinValueValidator


class login_credentials(models.Model):
    user_id = models.IntegerField(primary_key=True,validators = [MinValueValidator(0)])
    email = models.CharField(max_length=30, unique = True)
    password = models.CharField(max_length=30)
    def get_unique_id(self):
        return str(hash(self.email))

    def save(self, *args, **kwargs):
        self.user_id = self.get_unique_id()
        super(login_credentials, self).save(*args,**kwargs)
class users(models.Model):
    user_id = models.ForeignKey(login_credentials,on_delete=models.CASCADE)
    username = models.CharField(primary_key=True,max_length=15)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    SEX_CHOICES = [
    ('m','Male'),
    ('f','Female')
    ]
    sex = models.CharField(max_length=1, choices=SEX_CHOICES,default='m')
    nationality = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    #Below function is being used to calculate age as derived attribute
    def __str__(self):
        today = date.today()
        delta = relativedelta(today, self.date_of_birth)
        return str(delta.years)

    profile_picture = models.ImageField(upload_to="user_images/",default='')
    about_user = models.TextField(max_length=30)
