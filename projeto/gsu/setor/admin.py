from django.contrib import admin
from .models import Setor, Servico, Diretoria
# Register your models here.

@admin.register(Setor)
class SetorAdmin(admin.ModelAdmin):
	list_display = (
		'__str__',
	)
	# search_fields = ('algo',)
	# list_filter = ('algo',)


@admin.register(Diretoria)
class DiretoriaAdmin(admin.ModelAdmin):
    	list_display = (
		'__str__',
	)


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    	list_display = (
		'__str__',
	)
