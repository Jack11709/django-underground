# pylint: disable=no-member
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView

from .models import Station, Zone, Line
from .serializers import StationSerializer, ZoneSerializer, LineSerializer


class StationList(ListCreateAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class StationDetail(RetrieveUpdateDestroyAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

class ZoneList(ListAPIView):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer

class ZoneDetail(RetrieveAPIView):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer

class LineList(ListAPIView):
    queryset = Line.objects.all()
    serializer_class = LineSerializer

class LineDetail(RetrieveAPIView):
    queryset = Line.objects.all()
    serializer_class = LineSerializer
