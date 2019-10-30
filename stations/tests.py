# pylint: disable=no-member
from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Zone, Line, Station

class StationsTest(APITestCase):

    def setUp(self):
        zone = Zone.objects.create(zone=1)
        lines = Line.objects.create(name='District')
        station = Station.objects.create(
            name='Aldgate East',
            lat=51.5153,
            lon=0.0722,
            is_night_tube=False,
            zone=zone
        )
        station.lines.set([lines])

    def test_station_index(self):
        '''
        Should return an array of stations
        '''

        url = reverse('stations-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            response.content,
            [{
                'id': 1,
                'name': 'Aldgate East',
                'lat': 51.5153,
                'lon': 0.0722,
                'is_night_tube': False,
                'zone': {
                    'id': 1,
                    'zone': 1
                },
                'lines': [{
                    'id': 1,
                    'name': 'District'
                }]
            }]
        )

    def test_station_show(self):
        '''
        Should return a single Station Object
        '''

        url = ('/stations/1')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content,
            {
                'id': 1,
                'name': 'Aldgate East',
                'lat': 51.5153,
                'lon': 0.0722,
                'is_night_tube': False,
                'zone': {
                    'id': 1,
                    'zone': 1
                },
                'lines': [{
                    'id': 1,
                    'name': 'District'
                }]
            }
        )
