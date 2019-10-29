from django.urls import path
from .views import StationList, StationDetail

urlpatterns = [
    path('', StationList.as_view()),
    path('<int:pk>/', StationDetail.as_view())
]