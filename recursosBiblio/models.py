from django.db import models

# Create your models here.



class Author (models.Model) :
    DNI = models.BigIntegerField(primary_key=True)
    nom = models.TextField()
    cognom = models.TextField()
    nacionalidad = models.TextField()


class Biblioteca (models.Model) :
    id_biblio = models.BigIntegerField(primary_key=True)
    nom = models.TextField()
    ciutat = models.TextField()
    codi_postal = models.TextField()
    carrer = models.TextField()


class Book (models.Model) :
    ISBN = models.BigIntegerField(primary_key=True)
    titol = models.TextField()
    genere = models.TextField()
    edicio = models.TextField()
    numpages = models.IntegerField()
    author = models.ManyToManyField(Author, related_name='escrit_per')
    biblioteca=models.ManyToManyField(Biblioteca, related_name='disposa_de')



