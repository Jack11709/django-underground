from rest_framework import serializers
from .models import Station, Zone

class ZoneSerializer(serializers.ModelSerializer):

    class Meta:
      model = Zone
      fields = ('id', 'zone')

class StationSerializer(serializers.ModelSerializer):

    zone = ZoneSerializer()

    class Meta:
        model = Station
        fields = ('id', 'name', 'lat', 'lon', 'is_night_tube', 'zone')
        