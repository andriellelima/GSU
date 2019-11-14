from django.contrib import admin
from gsu.base.models import Setor, Servico


# admin.site.register(Setor)
# admin.site.register(Usuario)

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
