from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import CityNameSearchCounter


router = DefaultRouter()
router.register(r'city-search', CityNameSearchCounter, basename='cityname')

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
]
