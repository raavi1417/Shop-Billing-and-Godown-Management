# Generated by Django 3.0.8 on 2020-07-09 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_cart_pid'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
