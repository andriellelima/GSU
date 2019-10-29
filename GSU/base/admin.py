from django.contrib import admin

# Register your models here.
from base.models import Setor
from base.models import Usuario


admin.site.register(Setor)
admin.site.register(Usuario)