from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class general_information(models.Model):
    version_id = models.IntegerField(primary_key=True,validators = [MinValueValidator(0)])
    patch_notes = models.TextField(max_length=30)
    number_of_users = models.IntegerField(validators = [MinValueValidator(0)])
    copyright_notice = models.TextField(max_length=30)
    t_n_c = models.TextField(max_length=30)
