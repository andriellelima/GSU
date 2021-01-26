from django.contrib import admin
from gsu.base.models import Usuario
from .models import *
from django.contrib.auth.models import Permission
from django.contrib import admin


@admin.register(Setor)
class SetorAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
    )
    # fields = ('nome','descricao','responsavel','localizacao','horario_inicio','horario_fim')
    def get_queryset(self, request):
        qs = super(SetorAdmin, self).get_queryset(request)

        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()



@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
    )

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(ServicoAdmin, self).get_queryset(request)

        if request.user.is_superuser:
            return qs
        return qs.filter(setor__user = request.user)
