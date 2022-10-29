# Generated by Django 3.2.16 on 2022-10-29 12:47

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0014_alter_reservation_number_of_guests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date_time',
            field=models.DateTimeField(null=True, validators=[django.core.validators.MinValueValidator(datetime.datetime(2022, 10, 29, 12, 47, 33, 781092, tzinfo=utc), 'Please ensure your booking is from today onwards')]),
        ),
    ]
