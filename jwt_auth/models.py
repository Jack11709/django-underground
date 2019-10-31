from django.db import models
from django.contrib.auth.models import AbstractUser
# from stations.models import Station

class User(AbstractUser):

    image = models.CharField(max_length=500, blank=True)
    # favourite_station = models.ForeignKey(Station, related_name='favourited_by', on_delete=models.DO_NOTHING,null=True)