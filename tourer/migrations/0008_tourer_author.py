# Generated by Django 2.1 on 2018-10-09 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourer', '0007_remove_tourer_time_create'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourer',
            name='author',
            field=models.CharField(default='account', max_length=250),
        ),
    ]