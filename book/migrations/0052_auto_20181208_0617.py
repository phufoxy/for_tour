# Generated by Django 2.1 on 2018-12-07 23:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0051_auto_20181207_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album_tour',
            name='date_up',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 8, 6, 17, 47, 201250)),
        ),
        migrations.AlterField(
            model_name='book_tour',
            name='date_book',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 8, 6, 17, 47, 197759)),
        ),
        migrations.AlterField(
            model_name='book_tour',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 8, 6, 17, 47, 198257)),
        ),
        migrations.AlterField(
            model_name='house_tour',
            name='date_book',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 8, 6, 17, 47, 200252)),
        ),
        migrations.AlterField(
            model_name='house_tour',
            name='date_to',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 8, 6, 17, 47, 200252)),
        ),
        migrations.AlterField(
            model_name='place_tour',
            name='date_book',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 8, 6, 17, 47, 198757)),
        ),
        migrations.AlterField(
            model_name='place_tour',
            name='date_to',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 8, 6, 17, 47, 198757)),
        ),
        migrations.AlterField(
            model_name='restaurant_tour',
            name='date_book',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 8, 6, 17, 47, 198257)),
        ),
        migrations.AlterField(
            model_name='restaurant_tour',
            name='date_to',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 8, 6, 17, 47, 198257)),
        ),
        migrations.AlterField(
            model_name='vehicle_tour',
            name='date_book',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 8, 6, 17, 47, 199255)),
        ),
        migrations.AlterField(
            model_name='vehicle_tour',
            name='date_to',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 8, 6, 17, 47, 199255)),
        ),
    ]