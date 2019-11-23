from django.contrib import admin
from .models import Sugestao


@admin.register(Sugestao)
class SugestaoAdmin(admin.ModelAdmin):
    	list_display = (
		'__str__',
	)
