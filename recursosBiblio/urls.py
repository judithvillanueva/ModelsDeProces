from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic import ListView
from .models import *
from .views import *


urlpatterns = [
    url(r'^$',
        ListView.as_view(
            queryset=Book.objects.all(),            #bases de dades
            context_object_name = 'home',       #nom del diccionari
            template_name='recursosBiblio/home.html'), #posem el nom del html i on ho va a buscar
        name='home'),

    url(r'^buscador/$',
        buscador,
        name='buscador'),

    url(r'^llibres/$',
        ListView.as_view(
            queryset=Book.objects.all(),  # bases de dades
            context_object_name='llibres',  # nom del diccionari
            template_name='recursosBiblio/llibres.html'),  # posem el nom del html i on ho va a buscar
        name='llibres'),
]