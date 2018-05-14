
from __future__ import unicode_literals

from django.contrib import admin 
from import_export.admin import ImportExportModelAdmin 
from .models import Fila_datos, Lista
from import_export import resources 
	
# Register your models here. 


class ListaResource(resources.ModelResource): 
	class Meta: 
		model = Lista 
		exclude = ('imported')
		fields = ('id', 'Titular', 'Entradilla', 'Expresiones', 'Medio', 'URLNoticia', 'Fecha')

class ListaAdmin(ImportExportModelAdmin): 
	resource_class = ListaResource 
	list_display = ['Titular'] 

admin.site.register(Lista,ListaAdmin)