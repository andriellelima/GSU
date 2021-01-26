from django.contrib import admin
from .models import Sugestao, Usuario


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    	list_display = (
		'__str__',
	)

@admin.register(Sugestao)
class SugestaoAdmin(admin.ModelAdmin):
    	list_display = (
		'__str__',
	)
