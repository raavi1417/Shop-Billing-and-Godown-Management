# Generated by Django 3.0.8 on 2020-07-10 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0015_auto_20200711_0057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill',
            old_name='name',
            new_name='cust_name',
        ),
    ]
