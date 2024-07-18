import json
import requests


lat = '55.535289'
lon = '28.645541'
tup = (lat, lon)


def get_weather_data(coordinate_tuple: tuple) ->tuple:
    """these func connect to the Yandex server and receives data about weather"""
    definition_of_conditions = '5b90f809-9aa1-481d-8ad8-01ca2c7f40fb'
    headers = {
        'X-Yandex-Weather-Key': definition_of_conditions
    }
    lat = coordinate_tuple[0]
    lon = coordinate_tuple[1]
    response = requests.get(f'https://api.weather.yandex.ru/v2/forecast?lat={lon}&lon={lat}', headers=headers)
    data = response.json()
    # humidity = response.json()['fact']['humidity']
    cloudness = response.json()['fact']['cloudness']
    # feels_like = response.json()['fact']['feels_like']
    # pressure_mm = response.json()['fact']['pressure_mm']
    # temp = response.json()['fact']['temp']
    # wind_speed = response.json()['fact']['wind_speed']
    # print(json.dumps(response.json(), indent=4))

    # return humidity, cloudness, feels_like, pressure_mm, temp, wind_speed, data
    return data, cloudness

# get_weather_data(tup)