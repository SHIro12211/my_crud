from django.db import models
from django.forms import ModelForm


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=50)
    ci = models.IntegerField()
    age = models.IntegerField()
    sex = models.BooleanField()

    def __str__(self):
        return self.name


class PersonForm(ModelForm):
    class Meta:
        models = Person
        fields = ['name', 'ci', 'age', 'sex']
