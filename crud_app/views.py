from django.shortcuts import render, redirect, get_object_or_404

from .form import PersonForm
from .models import Person


def index(request):
    list = Person.objects.all()
    return render(request, "index.html", {'list': list})


def add(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud:index')
    else:
        form = PersonForm()
        return render(request, 'add.html', {'form': form})


def delete(request, id):
    p = get_object_or_404(Person, pk=id)
    p.delete()
    return redirect('crud:index')


def update(request, id):
    p = Person.objects.get(pk=id)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
            return redirect('crud:index')
    else:
        form=PersonForm(instance=p)
        return render(request, 'add.html', {'form':form})
