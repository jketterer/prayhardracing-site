from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^about$', views.about, name='about'),
    url('^big-cars$', views.bigCars, name='big-cars'),
    url('^juniors$', views.juniors, name='juniors'),
]
