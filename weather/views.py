from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            City.objects.all().delete()
            form.save()

    form = CityForm()
    all_cities_names = []
    cities_names = City.objects.all()

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
        'form': form
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
