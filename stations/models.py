from django.db import models

class Station(models.Model):
    name = models.CharField(max_length=100, unique=True)
    lat = models.FloatField()
    lon = models.FloatField()
    is_night_tube = models.BooleanField()

    def __str__(self):
        return f'{self.name}'
        