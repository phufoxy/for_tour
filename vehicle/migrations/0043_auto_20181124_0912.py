# Generated by Django 2.1 on 2018-11-24 02:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0042_auto_20181123_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_vehicle',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 24, 9, 12, 4, 911417)),
        ),
    ]
