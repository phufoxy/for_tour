# Generated by Django 2.1 on 2018-11-23 15:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0032_auto_20181123_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_restaurant',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 23, 22, 29, 57, 675492)),
        ),
    ]