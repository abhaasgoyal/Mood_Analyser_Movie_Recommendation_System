from django.db import models
from dateutil.relativedelta import relativedelta
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class User_Profile_Info(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=30, default='')
    # Additional
    SEX_CHOICES = [
    ('m','Male'),
    ('f','Female')
    ]
    sex = models.CharField(max_length=1, choices=SEX_CHOICES,default='m')
    nationality = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    #Below function is being used to calculate age as derived attribute


    profile_picture = models.ImageField(upload_to="user_images/",blank=True)
    about_user = models.TextField(max_length=30, default='')
    #
    # def __str__(self):
    #     today = date.today()
    #     delta = relativedelta(today, self.date_of_birth)
    #     return str(delta.years)
    # user_idz = models.IntegerField(validators = [MinValueValidator(0)])
    # def get_unique_id(self):
    #     return str(hash(self.about_user))
    #
    # def save(self, *args, **kwargs):
    #     self.user_id = self.get_unique_id()
    #     super(login_credentials, self).save(*args,**kwargs)


# class login_credentials(models.Model):
#     user_id = models.IntegerField(primary_key=True,validators = [MinValueValidator(0)])
#     email = models.CharField(max_length=30, unique = True)
#     password = models.CharField(max_length=30)
#     def get_unique_id(self):
#         return str(hash(self.email))
#
#     def save(self, *args, **kwargs):
#         self.user_id = self.get_unique_id()
#         super(login_credentials, self).save(*args,**kwargs)
