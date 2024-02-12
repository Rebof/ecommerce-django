

from django.shortcuts import render
from store.models import Store

def home(request):
    prod = Store.objects.all().filter(is_available=True)
    context = {
        'products' : prod
    }
    return render(request, 'home.html', context)