# Generated by Django 2.2.6 on 2019-10-30 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jwt_auth', '0002_user_favourite_station'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='favourite_station',
        ),
    ]
