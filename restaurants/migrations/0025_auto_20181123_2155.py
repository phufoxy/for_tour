# Generated by Django 2.1 on 2018-11-23 14:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0024_auto_20181123_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_restaurant',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 23, 21, 55, 53, 506789)),
        ),
    ]
