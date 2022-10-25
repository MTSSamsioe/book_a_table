from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
import django.utils.timezone


STATUS =  ((0, 'Draft'), (1, 'Published'))


# Create your models here.
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null= True)
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


COMMENT_OK =  ((0, 'Draft'), (1, 'Published'))

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING , null=True)
    created = models.DateTimeField(auto_now_add = True)
    image  = CloudinaryField('image', default= 'placeholder')
    text = models.TextField()
    approved = models.IntegerField(choices = COMMENT_OK, default= 0)
    stars = models.IntegerField(default = 3, validators=[MaxValueValidator(5),
            MinValueValidator(1)])

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f" {self.user} on {self.created}"