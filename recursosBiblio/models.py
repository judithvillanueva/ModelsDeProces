from django.db import models

# Create your models here.
class Book (models.Model) :
    ISBN = models.BigIntegerField(primary_Key=True)
    titol = models.TextField()
    genere = models.TextField()
    edicio = models.TextField()
    numpages = models.IntegerField()