from .models import City
from django.forms import ModelForm, TextInput

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
                    'name': TextInput(attrs={
                            'class': "form-control",
                            'name': 'city_name',
                            'id': 'city_name',
                            'placeholder': 'Введите город'})
                  }