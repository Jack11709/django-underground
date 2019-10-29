from rest_framework import serializers
from .models import Station, Zone, Line

class LineSerializer(serializers.ModelSerializer):

  class Meta:
    model = Line
    fields = ('id', 'name')

class ZoneSerializer(serializers.ModelSerializer):

    class Meta:
      model = Zone
      fields = ('id', 'zone')

class StationSerializer(serializers.ModelSerializer):

    zone = ZoneSerializer()
    lines = LineSerializer(many=True)

    class Meta:
        model = Station
        fields = ('id', 'name', 'lat', 'lon', 'is_night_tube', 'zone', 'lines')
        