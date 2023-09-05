from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


def is_valid_city(city_name):
    API_key = '3282ec1d46e5008d2addb00cc147282b'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=Metric&appid={API_key}'
    response = requests.get(url).json()

    return 'cod' in response and response['cod'] == 200

def index(request):
    cities_names = City.objects.all()
    error_message = None

    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            input_city_name = form.cleaned_data['name']


            if is_valid_city(input_city_name):
                City.objects.all().delete()
                form.save()
            else:
                error_message = "Город не найден."

    else:
        form = CityForm()

    all_cities_names = []

    for city_name in cities_names:
        API_key = '3282ec1d46e5008d2addb00cc147282b'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name.name}&units=Metric&appid={API_key}'
        response = requests.get(url).json()
        city_info = {
            'city_name': city_name.name,
            'country': response['sys']['country'],
            'temp_now': response['main']['temp'],
            'temp_max': response['main']['temp_max'],
            'temp_min': response['main']['temp_min'],
            'pressure': response['main']['pressure'],
            'speed_wind': response['wind']['speed'],
            'icon': response['weather'][0]['icon']
        }
        all_cities_names.append(city_info)

    context = {
        'all_city_info': all_cities_names,
        'form': form,
        'error_message': error_message,  # Передаем сообщение об ошибке в контекст
    }

    return render(request, 'weather/index.html', context)



def information(request):
    creator_info = {'name': 'Имя создателя','bio': 'Краткое описание создателя сайта.',}

    context = {'creator_info': creator_info}
    return render(request, 'weather/index_info.html', context)



def about(request):
    creator_info = {}
    context = {}
    return render(request, 'weather/index_about.html', context)



def doc(request):
    creator_info = {}

    context = {}
    return render(request, 'weather/index_documentation.html', context)
