from django import forms

from .models import Person

option_sex = [
    (1, 'Masculino'),
    (2, 'Femenino')
]


class PersonForm(forms.ModelForm):
    class Meta:
        models = Person
        fields = '__all__'
        widget = {'sex': forms.RadioSelect(choices=option_sex)}
