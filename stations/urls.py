from django.urls import path # included by default
from .views import StationList, StationDetail, ZoneList, ZoneDetail, LineList, LineDetail # import our DRF views

urlpatterns = [
    path('stations', StationList.as_view()),
    path('stations/<int:pk>/', StationDetail.as_view()),
    path('zones', ZoneList.as_view()),
    path('zones/<int:pk>/', ZoneDetail.as_view()),
    path('lines', LineList.as_view()),
    path('lines/<int:pk>/', LineDetail.as_view())
] # registering all our urls for this project, the route url for this project is in /project/urls.py