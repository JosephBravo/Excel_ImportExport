from __future__ import unicode_literals
from Prot1 import settings
from django.db import models

# Create your models here.

class Fila_datos(models.Model):
	contenido = models.TextField(blank=False, null=False)

class Lista(models.Model):
	Titular = models.TextField()
	Entradilla = models.TextField()
	Expresiones = models.TextField()
	Medio = models.TextField()
	URLNoticia = models.TextField()
	Fecha = models.DateField()