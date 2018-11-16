# Generated by Django 2.1 on 2018-11-16 09:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_auto_20181116_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album_tour',
            name='date_up',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 16, 16, 47, 59, 964928)),
        ),
        migrations.AlterField(
            model_name='book_tour',
            name='date_book',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 16, 16, 47, 59, 959932)),
        ),
        migrations.AlterField(
            model_name='book_tour',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 16, 16, 47, 59, 959932)),
        ),
        migrations.AlterField(
            model_name='house_tour',
            name='date_book',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 16, 16, 47, 59, 962930)),
        ),
        migrations.AlterField(
            model_name='house_tour',
            name='date_to',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 16, 16, 47, 59, 962930)),
        ),
        migrations.AlterField(
            model_name='place_tour',
            name='date_book',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 16, 16, 47, 59, 960931)),
        ),
        migrations.AlterField(
            model_name='place_tour',
            name='date_to',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 16, 16, 47, 59, 960931)),
        ),
        migrations.AlterField(
            model_name='restaurant_tour',
            name='date_book',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 16, 16, 47, 59, 959932)),
        ),
        migrations.AlterField(
            model_name='restaurant_tour',
            name='date_to',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 16, 16, 47, 59, 959932)),
        ),
        migrations.AlterField(
            model_name='vehicle_tour',
            name='date_book',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 16, 16, 47, 59, 961931)),
        ),
        migrations.AlterField(
            model_name='vehicle_tour',
            name='date_to',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 16, 16, 47, 59, 961931)),
        ),
    ]