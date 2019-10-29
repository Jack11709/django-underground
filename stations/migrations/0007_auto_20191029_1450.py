# Generated by Django 2.2.6 on 2019-10-29 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0006_station_lines'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='zone',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='stations', to='stations.Zone'),
        ),
    ]