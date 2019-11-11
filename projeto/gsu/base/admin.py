from django.contrib import admin
from gsu.base.models import Setor, Usuario, Servico


# admin.site.register(Setor)
# admin.site.register(Usuario)

@admin.register(Setor)
@admin.register(Usuario)
@admin.register(Servico)

class SetorAdmin(admin.ModelAdmin):
	list_display = (
		'__str__',
	)
	# search_fields = ('produto',)
	# list_filter = ('genero',)
