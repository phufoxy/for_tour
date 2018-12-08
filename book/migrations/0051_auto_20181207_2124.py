# Generated by Django 2.1 on 2018-12-07 14:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0050_auto_20181207_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album_tour',
            name='date_up',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 7, 21, 24, 5, 785767)),
        ),
        migrations.AlterField(
            model_name='book_tour',
            name='date_book',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 7, 21, 24, 5, 783272)),
        ),
        migrations.AlterField(
            model_name='book_tour',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 7, 21, 24, 5, 783272)),
        ),
        migrations.AlterField(
            model_name='house_tour',
            name='date_book',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 7, 21, 24, 5, 784769)),
        ),
        migrations.AlterField(
            model_name='house_tour',
            name='date_to',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 7, 21, 24, 5, 784769)),
        ),
        migrations.AlterField(
            model_name='place_tour',
            name='date_book',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 7, 21, 24, 5, 783771)),
        ),
        migrations.AlterField(
            model_name='place_tour',
            name='date_to',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 7, 21, 24, 5, 783771)),
        ),
        migrations.AlterField(
            model_name='restaurant_tour',
            name='date_book',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 7, 21, 24, 5, 783272)),
        ),
        migrations.AlterField(
            model_name='restaurant_tour',
            name='date_to',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 7, 21, 24, 5, 783272)),
        ),
        migrations.AlterField(
            model_name='vehicle_tour',
            name='date_book',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 7, 21, 24, 5, 784270)),
        ),
        migrations.AlterField(
            model_name='vehicle_tour',
            name='date_to',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 7, 21, 24, 5, 784270)),
        ),
    ]