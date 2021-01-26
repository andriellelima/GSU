from django.contrib import admin
from .models import Sugestao, Usuario
from django.contrib.auth.models import Permission
from django.contrib import admin
from .forms import UsuarioForm
from django.db.models import Q

@admin.register(Usuario)
class UserAdmin(admin.ModelAdmin):
	form = UsuarioForm
	def save_model(self, request, obj, form, change):
		obj.save()
		obj.user_permissions.clear()
		permissions = Permission.objects.filter(Q(codename__endswith="setor") | Q(codename__endswith="servico"))
		for permission in permissions:		
			obj.user_permissions.add(permission)	
		obj.is_staff = True
		super().save_model(request, obj, form, change)

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
