# pylint: disable=no-member
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Station, Zone, Line
from .serializers import StationSerializer, ZoneSerializer, LineSerializer


class StationList(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly ,)
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class StationDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly ,)
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
