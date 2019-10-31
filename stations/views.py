# pylint: disable=no-member
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .permissions import isOwnerOrReadOnly
from .models import Station, Zone, Line
from .serializers import StationSerializer, ZoneSerializer, LineSerializer


class StationList(ListCreateAPIView):
    permission_classes = (isOwnerOrReadOnly ,)
    queryset = Station.objects.all()
    serializer_class = StationSerializer

    def post(self, request):
        serializer = StationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=422)


class StationDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (isOwnerOrReadOnly ,)
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    # ! this is not working, not merging with existing fields
    def patch(self, request, pk):
        station = Station.objects.get(pk=pk)
        serializer = StationSerializer(station, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=422)

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
