from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Setor)
class SetorAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
    )

    # def save_model(self, request, obj, form, change):
    #     obj.user = request.user
    #     obj.save()

    def get_queryset(self, request):
        qs = super(SetorAdmin, self).get_queryset(request)

        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


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
        return qs.filter(user=request.user)
