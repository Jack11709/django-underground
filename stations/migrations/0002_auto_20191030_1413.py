# Generated by Django 2.2.6 on 2019-10-30 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='zone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='stations', to='stations.Zone'),
        ),
    ]