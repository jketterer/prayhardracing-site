from django.shortcuts import render
from .models import Driver, About

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def about(request):

    info = About.objects.all()

    context = {
        'Info': info,
    }

    return render(request, 'home/about.html', context)

def bigCars(request):

    drivers = []

    for driver in Driver.objects.all():
        if not driver.junior:
            drivers.append(driver)

    context = {
        'Drivers': drivers,
        'Title': "Big Car Drivers"
    }

    return render(request, 'home/drivers.html', context)

def juniors(request):

    drivers = []

    for driver in Driver.objects.all():
        if driver.junior:
            drivers.append(driver)

    context = {
        'Drivers': drivers,
        'Title': "Junior Drivers",
    }

    return render(request, 'home/drivers.html', context)
