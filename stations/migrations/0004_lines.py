# Generated by Django 2.2.6 on 2019-10-29 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0003_station_zone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]