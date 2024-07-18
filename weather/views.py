from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import CityName, UsersLastSearch
from .forms import CityForm
from .services.converting_cities_to_coordinates import convert_city_to_coordinate
from .services.get_weather_from_api import get_weather_data
from .services.cloud_check import cloud_check
from rest_framework import viewsets
from .models import CityName
from .serializers import CityNameSerializer


def index(request):
    user_id = request.COOKIES.get('user_id')
    if user_id:
        last_search = UsersLastSearch.objects.filter(user_id=user_id).select_related('city_name').order_by('-last_searched').first()
        if last_search and last_search.city_name.id:
            message = f'Рады вас видеть снова, в прошлый раз вы искали погоду в городе: {last_search.city_name}'
        else:
            message = f'Рады вас видеть снова!'
    else:
        user_id = UsersLastSearch.objects.order_by('-user_id').first().user_id + 1
        message = "Добро пожаловать! Введите название города для прогноза погоды."

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['city_name']
            city_name = city_name[0].upper() + city_name[1:].lower()
            city, created = CityName.objects.get_or_create(city_name=city_name)
            if created:
                city.count_of_search = 1
            else:
                city.count_of_search += 1
            city.save()
            UsersLastSearch.objects.create(user_id=user_id, city_name=city)
            convert_data = convert_city_to_coordinate(city_name)
            get_weather_data_from_website = get_weather_data(convert_data)
            cloud_check_result = cloud_check(get_weather_data_from_website[1])
            weather_data = get_weather_data_from_website[0]
            response = render(request, 'weather/index.html', {
                                                            'form': form,
                                                            'weather_data': weather_data,
                                                            'cloud_check_result': cloud_check_result,
                                                            'city_name': city_name,
                                                            })
            response.set_cookie('user_id', user_id)
            return response
    else:
        form = CityForm()
    response = render(request, 'weather/index.html', {'form': form, 'message': message})
    response.set_cookie('user_id', user_id)
    return response


class CityNameSearchCounter(viewsets.ReadOnlyModelViewSet):
    '''these func returned json with the city name and amount of search'''
    queryset = CityName.objects.all()
    serializer_class = CityNameSerializer
