# Generated by Django 3.0.8 on 2020-07-09 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_auto_20200710_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='price',
            field=models.IntegerField(),
        ),
    ]