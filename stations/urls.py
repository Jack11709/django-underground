from django.urls import path 
from .views import StationList, StationDetail, ZoneList, ZoneDetail, LineList, LineDetail # import our DRF views

urlpatterns = [
    path('stations', StationList.as_view(), name='stations-list'),
    path('stations/<int:pk>/', StationDetail.as_view(), name='stations-detail'),
    path('zones', ZoneList.as_view()),
    path('zones/<int:pk>/', ZoneDetail.as_view()),
    path('lines', LineList.as_view()),
    path('lines/<int:pk>/', LineDetail.as_view())
] # registering all our urls for this project, the route url for this project is in /project/urls.py