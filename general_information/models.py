from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class general_information(models.Model):
    patch_date = models.DateTimeField(blank=True, null=True)
    version_id = models.IntegerField(primary_key=True,validators = [MinValueValidator(0)])
    patch_notes = models.TextField(max_length=1000)
    number_of_users = models.IntegerField(validators = [MinValueValidator(0)])
    copyright_notice = models.TextField(max_length=1000)
    t_n_c = models.TextField(max_length=30)
