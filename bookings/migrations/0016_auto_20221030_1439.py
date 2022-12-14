# Generated by Django 3.2.16 on 2022-10-30 13:39

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0015_alter_reservation_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='text',
            field=models.TextField(max_length=400),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_time',
            field=models.DateTimeField(null=True, validators=[django.core.validators.MinValueValidator(datetime.datetime(2022, 10, 30, 13, 39, 7, 174355, tzinfo=utc), 'Please pick a date and time before present time')]),
        ),
    ]
