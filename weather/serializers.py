from rest_framework import serializers
from .models import CityName


class CityNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityName
        fields = ['city_name', 'count_of_search']
