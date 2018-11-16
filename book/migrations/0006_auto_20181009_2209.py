# Generated by Django 2.1 on 2018-10-09 15:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20181009_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album_tour',
            name='date_up',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 9, 22, 9, 39, 779504)),
        ),
        migrations.AlterField(
            model_name='book_tour',
            name='date_book',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 9, 22, 9, 39, 776507)),
        ),
        migrations.AlterField(
            model_name='book_tour',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 9, 22, 9, 39, 776507)),
        ),
        migrations.AlterField(
            model_name='house_tour',
            name='date_book',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 9, 22, 9, 39, 778501)),
        ),
        migrations.AlterField(
            model_name='house_tour',
            name='date_to',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 9, 22, 9, 39, 778501)),
        ),
        migrations.AlterField(
            model_name='place_tour',
            name='date_book',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 9, 22, 9, 39, 777506)),
        ),
        migrations.AlterField(
            model_name='place_tour',
            name='date_to',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 9, 22, 9, 39, 777506)),
        ),
        migrations.AlterField(
            model_name='restaurant_tour',
            name='date_book',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 9, 22, 9, 39, 776507)),
        ),
        migrations.AlterField(
            model_name='restaurant_tour',
            name='date_to',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 9, 22, 9, 39, 776507)),
        ),
        migrations.AlterField(
            model_name='vehicle_tour',
            name='date_book',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 9, 22, 9, 39, 777506)),
        ),
        migrations.AlterField(
            model_name='vehicle_tour',
            name='date_to',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 9, 22, 9, 39, 777506)),
        ),
    ]