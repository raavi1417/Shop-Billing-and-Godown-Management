# Generated by Django 3.0.8 on 2020-07-28 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0023_auto_20200728_1648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='stock_date',
        ),
    ]
