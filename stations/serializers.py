# pylint: disable=no-member
from rest_framework import serializers
from .models import Station, Zone, Line
from jwt_auth.serializers import UserSerializer

class NestedStationSerializer(serializers.ModelSerializer): # making use of our nested serializers, this is solving two problems, one, trying to references certain models before they are instantited, for example, we want to show stations on lines and lines on stations, we need one of them to come first. Also fixing the issues of circuluar referencing

    class Meta:
        model = Station
        fields = ('id', 'name', 'lat', 'lon', 'is_night_tube')

class NestedZoneSerializer(serializers.ModelSerializer): # creating these nested serializers first, so they can be used in the 'real' serializers below. these nested versions do not include the field in which they will be nexted, therefore not creating a circuluar reference. EG This nested zone serialiser does not include the stations in its fields, so it can be nested in the station serializer without creating a circular reference.

    class Meta:
        model = Zone
        fields = ('id', 'zone')

class NestedLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Line
        fields = ('id', 'name')

class StationSerializer(serializers.ModelSerializer):

    zone = NestedZoneSerializer() # here is that nested serializer being used
    lines = NestedLineSerializer(many=True)
    owner = UserSerializer()

    def create(self, data):
        zone_data = data.pop('zone')
        lines_data = data.pop('lines')

        station = Station(**data)
        station.zone = Zone.objects.get(**zone_data)
        lines = [Line.objects.get(**line_data) for line_data in lines_data]
        station.save() # <=== this was key to ensure the primary key existed before trying to make the nested MTM relationship
        station.lines.set(lines)
        return station

    class Meta:
        model = Station
        fields = ('id', 'name', 'lat', 'lon', 'is_night_tube', 'zone', 'lines', 'owner') # and the adding of zone field with use that nested version, with no reference to station.

class ZoneSerializer(serializers.ModelSerializer):

    stations = NestedStationSerializer(many=True)

    class Meta:
        model = Zone
        fields = ('id', 'zone', 'stations')

class LineSerializer(serializers.ModelSerializer):

    stations = NestedStationSerializer(many=True)

    class Meta:
        model = Line
        fields = ('id', 'name', 'stations')
