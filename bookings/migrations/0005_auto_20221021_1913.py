# Generated by Django 3.2.16 on 2022-10-21 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_auto_20221021_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.TimeField(),
        ),
    ]
