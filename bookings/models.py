from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime, timedelta
import django.utils.timezone
import math
from django.contrib import messages
import datetime
import pytz
from django.core.exceptions import ValidationError

# Choices for reservation model fields

STATUS = ((0, 'Not approved'), (1, 'Approved'))
GUESETS = ((1, '1'), (2, '2'), (3, '3'), (4, '4'),
           (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'),
           (10, '10'), (11, '11'), (12, '12'),)


# Model for making reservation

class Reservation(models.Model):
    """ Model to handle reservations  """

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=80, blank=False, null=False)
    last_name = models.CharField(max_length=80, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False, null=False)
    date_time = models.DateTimeField(null=True, blank=False,
                                     validators=[MinValueValidator
                                                 (datetime.datetime.utcnow()
                                                  .replace(tzinfo=pytz.UTC),
                                                  """Please pick a date
                                                  and time
                                                  after present time""")])
    date_time_end = models.DateTimeField(null=True)
    number_of_guests = models.IntegerField(
                                           default=2, blank=False, null=False,
                                           choices=GUESETS)
    number_of_tables = models.IntegerField(null=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-date_time']

    def __str__(self):
        return self.first_name

    # Function that prevent double bookings during a 120 minutes timeslot

    def clean(self):
        """ Model method to prevent reservations outside
        opening hours and before current """

        self.is_cleaned = True
        total_tables_for_two = 10
        date_time_form = self.date_time
        number_of_guests = self.number_of_guests
        tables_needed = math.ceil(number_of_guests / 2)
        reservations = Reservation.objects.all()
        for reservation in reservations:
            if reservation.date_time <= date_time_form and reservation. \
                    date_time_end >= date_time_form:

                tables_used = reservation.number_of_tables
                total_tables_for_two -= tables_used

        if tables_needed > total_tables_for_two:
            raise ValidationError("""No
            available tables during this time and date. Please try again""")

        # Conditional to prevent reservation outside opening hours
        if str(date_time_form)[11:13] > str(21):
            raise ValidationError("""pick a time before
             closing (last reservation time is before 22.00)""")
        if str(date_time_form)[11:13] < str(11):
            raise ValidationError("pick a time after opening")
        super(Reservation, self).clean()

    # Calc number of tables needed for reservation

    def save(self, *args, **kwargs):
        """ Model method to prevent double bookings"""

        if not self.number_of_tables:
            new_number_of_tables = math.ceil(self.number_of_guests / 2)
            self.number_of_tables = new_number_of_tables
        if not self.date_time_end:
            end_time = self.date_time + timedelta(minutes=120)
            self.date_time_end = end_time

        return super().save(*args, **kwargs)


COMMENT_OK = ((0, 'Draft'), (1, 'Published'))
STARS = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), )

# Model for leaving comments and reviews


class Comments(models.Model):
    """ Model to store comments """

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image', default='placeholder')
    text = models.TextField(max_length=400, blank=False, null=False)
    approved = models.IntegerField(choices=COMMENT_OK, default=0)
    stars = models.IntegerField(
                                default=3, choices=STARS,
                                blank=False, null=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return str(self.user)
