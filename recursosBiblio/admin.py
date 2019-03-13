from django.contrib import admin
from recursosBiblio import models

# Register your models here.
admin.site.register(models.Book)
admin.site.register(models.Biblioteca)
admin.site.register(models.Author)
