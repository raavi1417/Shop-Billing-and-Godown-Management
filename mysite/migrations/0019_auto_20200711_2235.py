# Generated by Django 3.0.8 on 2020-07-11 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0018_auto_20200711_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='mobile',
            field=models.CharField(max_length=12),
        ),
    ]
