# Generated by Django 2.1 on 2018-11-23 15:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0036_auto_20181123_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_vehicle',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 23, 22, 43, 23, 313269)),
        ),
    ]
