# Generated by Django 2.1 on 2018-11-23 15:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0035_auto_20181123_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_house',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 23, 22, 17, 27, 480618)),
        ),
    ]