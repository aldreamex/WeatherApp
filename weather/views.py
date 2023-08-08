from django.shortcuts import render
import requests
from .models import City

def index(request):
    cities_names = City.objects.all()
    all_cities_names = []
    for city_name in cities_names:
        API_key = '3282ec1d46e5008d2addb00cc147282b'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name.name}&units=Metric&appid={API_key}'
        response = requests.get(url).json()     #requests.get(url.format(city_name.name)).json()
        print(url)
        city_info = {
            'city_name': city_name.name,
            'temp_now': response['main']['temp'],
            'temp_max': response['main']['temp_max'],
            'temp_min': response['main']['temp_min'],
            'pressure': response['main']['pressure'],
            'speed_wind': response['wind']['speed'],
            'icon': response['weather'][0]['icon']
        }
        all_cities_names.append(city_info)

    context = {
        'all_city_info': all_cities_names
    }

    return render(request, 'weather/index.html', context)






# def index(request):
#
#     API_key = '3282ec1d46e5008d2addb00cc147282b'
#     url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=Metric&appid=' + API_key
#
#     # response = requests.get(url.format(city_name.name)).json()
#     cities = City.objects.all()
#     # print(cities)
#     all_cities = []
#     # print(all_cities)
#     for city in cities:
#         response = requests.get(url.format(city.name)).json()
#         print(cities)
#         city_info = {
#             'city_name': city.name,
#             'temp_now': response['main']['temp'],
#             'temp_max': response['main']['temp_max'],
#             'temp_min': response['main']['temp_min'],
#             'pressure': response['main']['pressure'],
#             'speed_wind': response['wind']['speed'],
#             'icon': response['weather'][0]['icon']
#         }
#     all_cities.append(city_info)
#
#     context = {
#         'all_city_info': all_cities
#     }
#
#     return render(request, 'weather/index.html', context)

# def index(request):
#
#     API_key = '3282ec1d46e5008d2addb00cc147282b'
#     url = f'https://api.openweathermap.org/data/2.5/weather?q={{}&units=Metric&appid={API_key}'
#
#     cities = City.objects.all()
#     all_cities = []
#
#     for city in cities:
#         response = requests.get(url.format(city.name)).json()
#
#         if response.get('cod') == '404':
#             error_info = {
#                 'city_name': city.name,
#                 'error_message': 'City not found'
#             }
#             all_cities.append(error_info)
#         else:
#             city_info = {
#                 'city_name': city.name,
#                 'temp_now': response['main']['temp'],
#                 'temp_max': response['main']['temp_max'],
#                 'temp_min': response['main']['temp_min'],
#                 'pressure': response['main']['pressure'],
#                 'speed_wind': response['wind']['speed'],
#                 'icon': response['weather'][0]['icon']
#             }
#             all_cities.append(city_info)
#
#     context = {
#         'all_city_info': all_cities  # Используйте список all_cities вместо city_info
#     }
#
#     return render(request, 'weather/index.html', context)


def information(request):
    creator_info = {
        'name': 'Имя создателя',
        'bio': 'Краткое описание создателя сайта.',
    }

    context = {
        'creator_info': creator_info
    }
    return render(request, 'weather/index_info.html', context)
