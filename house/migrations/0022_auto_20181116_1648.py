# Generated by Django 2.1 on 2018-11-16 09:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0021_auto_20181116_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='location',
        ),
        migrations.AddField(
            model_name='house',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='city',
            field=models.CharField(blank=True, choices=[('Đà Nẵng', 'Đà Nẵng'), ('Hà Nội', 'Hà Nội'), ('Hồ Chí Minh', 'Hồ Chí Minh'), ('Đà Lạt', 'Đà Lạt'), ('Nha Trang', 'Nha Trang'), ('Quảng Nam', 'Quảng Nam'), ('Quảng Ngãi', 'Quảng Ngãi'), ('Huế', 'Huế'), ('Gia Lai', 'Gia Lai'), ('Ninh Bình', 'Ninh Bình'), ('Quy Nhơn', 'Quy Nhơn')], default='Đà Nẵng', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='comment_house',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 16, 16, 47, 59, 943958)),
        ),
        migrations.AlterField(
            model_name='house',
            name='room_type',
            field=models.CharField(blank=True, choices=[('Đơn', 'Đơn'), ('Đôi', 'Đôi'), ('Ba', 'Ba')], default='Đơn', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='type_house',
            field=models.CharField(choices=[('Nhà Nghĩ', 'Nhà Nghĩ'), ('Khách Sạn', 'Khách Sạn'), ('Nhà Trọ', 'Nhà Trọ'), ('HomeStay', 'HomeStay')], default='Nhà Nghĩ', max_length=250),
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]