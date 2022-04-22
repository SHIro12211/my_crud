from .form import PersonForm


# Create your views here.
def add(request):
    if request.method == 'POST':
        try:
            from=PersonForm(request.POST)
