from django import forms


class CityForm(forms.Form):
    city_name = forms.CharField(label='Ведите название города', max_length=100)


