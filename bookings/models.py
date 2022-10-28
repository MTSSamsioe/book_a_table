from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator  # ta bort
from datetime import datetime, timedelta
import django.utils.timezone
import math
from django.contrib import messages  # tas bort

# ta bort
STATUS = ((0, 'Not approved'), (1, 'Approved'))
GUESETS = ((1, '1'), (2, '2'), (3, '3'), (4, '4'),
           (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'),
           (10, '10'), (11, '11'), (12, '12'),)

# Create your models here.


class Reservation(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date_time = models.DateTimeField(null=True)
    date_time_end = models.DateTimeField(null=True)
    number_of_guests = models.IntegerField(default=2, choices=GUESETS)  # validators=[MinValueValidator(1), MaxValueValidator(12)]
    number_of_tables = models.IntegerField(null=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ['-date_time']

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        if not self.number_of_tables:
            new_number_of_tables = math.ceil(self.number_of_guests / 2)
            self.number_of_tables = new_number_of_tables
        if not self.date_time_end:
            end_time = self.date_time + timedelta(minutes=120)
            self.date_time_end = end_time     
        return super().save(*args, **kwargs)


COMMENT_OK = ((0, 'Draft'), (1, 'Published'))
STARS = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), )


class Comments(models.Model):

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image', default='placeholder')
    text = models.TextField()
    approved = models.IntegerField(choices=COMMENT_OK, default=0)
    stars = models.IntegerField(default=3, choices=STARS)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f" {self.user} on {self.created}"
