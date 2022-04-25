from django.http import HttpRequest
from django.shortcuts import render

from .form import PersonForm


class PersonFormViews(HttpRequest):

    def add(request):
        form = PersonForm()
        if form.is_valid():
            form.save()
            form = PersonForm()
        return render(request, 'add.html', {'form': form})
