from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic import ListView
from .models import *


urlpatterns = [
    url(r'^$',
        ListView.as_view(
            queryset=Book.objects.all(),            #bases de dades
            context_object_name = 'AllBooks',       #nom del diccionari
            template_name='recursosBiblio/AllBooks.html'), #posem el nom del html i on ho va a buscar
        name='AllBooks')
]