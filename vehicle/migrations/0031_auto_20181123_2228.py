# Generated by Django 2.1 on 2018-11-23 15:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0030_auto_20181123_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_vehicle',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 23, 22, 28, 19, 938280)),
        ),
    ]
