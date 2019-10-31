from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Line(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

class Zone(models.Model):
    zone = models.IntegerField()

    def __str__(self):
        return f'{self.zone}'

# TODO how to make zone and line fields not required? This isnt working.
class Station(models.Model):
    name = models.CharField(max_length=100, unique=True)
    lat = models.FloatField()
    lon = models.FloatField()
    is_night_tube = models.BooleanField()
    zone = models.ForeignKey(
      Zone, 
      related_name='stations', 
      on_delete=models.DO_NOTHING, 
      null=True
    )
    lines = models.ManyToManyField(
        Line,
        related_name='stations',
        blank=True,
    )
    owner = models.ForeignKey(
        User, 
        related_name='stations', 
        on_delete=models.CASCADE, 
        null=True
    )

    def __str__(self):
        return f'{self.name}'
