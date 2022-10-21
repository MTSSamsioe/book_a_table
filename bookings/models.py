from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator

import django.utils.timezone


STATUS =  ((0, 'Draft'), (1, 'Published'))


# Create your models here.
class Reservation(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.IntegerField(default = 2, validators=[MaxValueValidator(12),
            MinValueValidator(1)])
    #featured_image = CloudinaryField('image', default = 'placeholder')
    status = models.IntegerField(choices = STATUS, default = 1)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.first_name

