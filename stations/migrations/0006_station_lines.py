# Generated by Django 2.2.6 on 2019-10-29 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0005_auto_20191029_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='lines',
            field=models.ManyToManyField(blank=True, related_name='stations', to='stations.Line'),
        ),
    ]