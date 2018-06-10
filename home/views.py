from django.shortcuts import render
from .models import Driver
from posts.models import Post

# Create your views here.
def index(request):

    recent = Post.objects.all()[:3]

    posts = {
        'post1': recent[0],
        'post2': recent[1],
        'post3': recent[2],
    }

    context = {
        'posts': posts,
    }

    return render(request, 'home/index.html', context)

def about(request):
    return render(request, 'home/about.html')

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
