from django.shortcuts import render

from django.http import HttpResponse

from .models import *

# Create your views here.



def buscador(request):
    option = request.POST['opcions']
    if option == "Book":
        resultats = Book.objects.filter(titol__contains=request.POST['buscar'])
        dictio = {'resultats': resultats,
                  'tipus': option}
        return render(request=request, template_name="recursosBiblio/resultats.html", context=dictio)

    elif option == "Author":
        resultats = Author.objects.filter(nom__contains=request.POST['buscar'])
        dictio = {'resultats': resultats,
                  'tipus': option}
        return render(request=request, template_name="recursosBiblio/resultats.html", context=dictio)

    elif option == "Biblioteca":
        resultats = Biblioteca.objects.filter(nom__contains=request.POST['buscar'])
        dictio = {'resultats': resultats,
                  'tipus': option}
        return render(request=request, template_name="recursosBiblio/resultats.html", context=dictio)


