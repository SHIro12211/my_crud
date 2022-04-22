from django import forms

option_sex = ['F', 'M']


class PersonForm(forms.Form):
    name_form = forms.CharField(label='Nombre', max_length=50)
    ci_form = forms.IntegerField(label='Carnet de ID')
    age_form = forms.IntegerField(label='Edad')
    sex_form = forms.BooleanField(
        label='Sexo',
        widget=forms.Select(choices=option_sex)
    )
