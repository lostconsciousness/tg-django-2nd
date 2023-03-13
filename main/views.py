from django.shortcuts import render
from main.models import Podik


def heater(request):
    context = {
        "pods": Podik.objects.all().filter(categoryId = 238)
    }
    return render(request, 'main/heater.html', context)

def homepage(request):
    return render(request, 'main/homepage.html', {})
# Create your views here.
