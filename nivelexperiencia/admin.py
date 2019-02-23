from django.contrib import admin

from .models import NivelExperiencia

class NivelExperienciaAdmin(admin.ModelAdmin):
    list_display = ('nivel', 'descricao')
    list_filter = ['descricao']
    search_fields = ['descricao']

admin.site.register(NivelExperiencia, NivelExperienciaAdmin)
