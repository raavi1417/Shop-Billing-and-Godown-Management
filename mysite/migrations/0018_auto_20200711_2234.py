# Generated by Django 3.0.8 on 2020-07-11 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0017_auto_20200711_0135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill',
            old_name='total',
            new_name='final',
        ),
    ]