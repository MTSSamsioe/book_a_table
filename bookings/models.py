from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
import django.utils.timezone


STATUS =  ((0, 'Not approved'), (1, 'Approved'))
GUESETS = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'),)

# Create your models here.
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null= True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.IntegerField(default = 2, choices = GUESETS)
    status = models.IntegerField(choices = STATUS, default = 1)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.first_name


COMMENT_OK =  ((0, 'Draft'), (1, 'Published'))
STARS = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), )

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING , null=True)
    created = models.DateTimeField(auto_now_add = True)
    image  = CloudinaryField('image', default= 'placeholder')
    text = models.TextField()
    approved = models.IntegerField(choices = COMMENT_OK, default= 0)
    stars = models.IntegerField(default = 3, choices= STARS)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f" {self.user} on {self.created}"