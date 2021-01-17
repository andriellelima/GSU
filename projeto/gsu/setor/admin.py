from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Setor)
class SetorAdmin(admin.ModelAdmin):
	list_display = (
		'__str__',
	)
	# search_fields = ('algo',)
	# list_filter = ('algo',)



@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    	list_display = (
		'__str__',
	)
