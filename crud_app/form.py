from django import forms

from .models import Person

OPTION_SEX = [
    (1, 'Masculino'),
    (2, 'Femenino')
]


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        labels = {
            'sex': 'Sexo'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'name'}),

            'sex': forms.RadioSelect(choices=OPTION_SEX)
        }
