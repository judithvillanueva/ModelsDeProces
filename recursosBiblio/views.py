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


def detalls_autor(request, pk):
    autor = Author.objects.get(pk=pk)
    resultats = Book.objects.filter(author=autor)
    dictio = {'llibres': resultats,
              'autor': autor}
    return render(request=request, template_name="recursosBiblio/detalls_autor.html", context=dictio)

def detalls_biblio(request, pk):
    biblio = Biblioteca.objects.get(pk=pk)
    resultats = Book.objects.filter(biblioteca=biblio.id_biblio)
    dictio = {'llibres': resultats,
              'biblio': biblio}
    return render(request=request, template_name="recursosBiblio/detalls_biblio.html", context=dictio)

