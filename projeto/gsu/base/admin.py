from django.contrib import admin
from .models import Sugestao, Usuario
from django.contrib.auth.models import Permission
from django.contrib import admin
from .forms import *
from django.db.models import Q
from django.contrib.auth.admin import UserAdmin


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
	add_form = UsuarioForm
	form = UsuarioChangeForm
	list_display = (
		'__str__',
		)

	def get_queryset(self, request):
		qs = super(UsuarioAdmin, self).get_queryset(request)

		if request.user.is_superuser:
			return qs
		return qs.filter(user=request.user)
	def save_model(self, request, obj, form, change):
		obj.save()
		obj.user_permissions.clear()
		permissions = Permission.objects.filter(Q(codename__endswith="setor") | Q(codename__endswith="servico"))
		for permission in permissions:		
			obj.user_permissions.add(permission)	
		obj.is_staff = True
		super().save_model(request, obj, form, change)
		
	def get_form(self, request, obj=None, **kwargs):
		defaults = {}
		if obj is None:
			defaults['form'] = self.add_form
		defaults.update(kwargs)
		return super().get_form(request, obj, **defaults)
		
		

    	

@admin.register(Sugestao)
class SugestaoAdmin(admin.ModelAdmin):
    	list_display = (
		'__str__',
	)
