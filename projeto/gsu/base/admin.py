from django.contrib import admin

# Register your models here.
from gsu.base.models import Setor
from gsu.base.models import Usuario


admin.site.register(Setor)
admin.site.register(Usuario)