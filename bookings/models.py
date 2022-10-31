from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator  # ta bort
from datetime import datetime, timedelta
import django.utils.timezone
import math
from django.contrib import messages  # tas bort
import datetime
import pytz
from django.core.exceptions import ValidationError


# ta bort
STATUS = ((0, 'Not approved'), (1, 'Approved'))
GUESETS = ((1, '1'), (2, '2'), (3, '3'), (4, '4'),
           (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'),
           (10, '10'), (11, '11'), (12, '12'),)

# Create your models here.


class Reservation(models.Model):
    is_cleaned = False
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=254)
    date_time = models.DateTimeField(null= True, validators=[MinValueValidator(datetime.datetime.utcnow().replace(tzinfo=pytz.UTC), "Please pick a date and time before present time")])
    date_time_end = models.DateTimeField(null=True)
    number_of_guests = models.IntegerField(default=2, choices=GUESETS)
    number_of_tables = models.IntegerField(null=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ['-date_time']

    def __str__(self):
        return self.first_name
    # available func
    def clean(self):
        self.is_cleaned = True
        total_tables_for_two = 10
        date_time_form = self.date_time
        #date_time_data_base = Reservation.objects.date_time.all()
        number_of_guests = self.number_of_guests
        tables_needed = math.ceil(number_of_guests / 2)
        #table_collide = Reservation.objects.filter(date_time__lte= date_time_form).filter(date_time_end__gte= date_time_form)
        reservations = Reservation.objects.all()
        for reservation in reservations:
            if reservation.date_time <= date_time_form and reservation.date_time_end >= date_time_form:

                tables_used = reservation.number_of_tables
                total_tables_for_two -= tables_used
        

        if tables_needed > total_tables_for_two:
            raise ValidationError("No tables")

        #if str(date_time_form)[12:13] > str(22) :
        #    raise ValidationError("pick a time before closing time")
        opening = '11:00'
        if str(date_time_form)[11:13] > str(21):
            raise ValidationError("pick a time before closing (last reservation time is before 22.00)")
        if str(date_time_form)[11:13] < str(11):
            raise ValidationError("pick a time after opening")
        super(Reservation, self).clean()
    
    # Calc number of tables
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
    text = models.TextField(max_length= 400)
    approved = models.IntegerField(choices=COMMENT_OK, default=0)
    stars = models.IntegerField(default=3, choices=STARS)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f" {self.user} on {self.created}"
