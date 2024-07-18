import requests
import json


def convert_data(response: dict, city: str) -> tuple or None:
    datas = response.json()['response']['GeoObjectCollection']['featureMember']
    for data in datas:
        geo_object = data['GeoObject']
        name = geo_object['name']
        if name == city:
            pos = geo_object['Point']['pos']
            lon, lat = map(float, pos.split())
            return lon, lat
    return None


def convert_city_to_coordinate(city: str) -> tuple:
    definition_of_conditions = '069b763f-5390-445a-9904-68f11c833bf9'
    url = f'https://geocode-maps.yandex.ru/1.x/?apikey={definition_of_conditions}&geocode={city}&format=json'
    response = requests.get(url)
    parsing_data = convert_data(response, city)
    return parsing_data
