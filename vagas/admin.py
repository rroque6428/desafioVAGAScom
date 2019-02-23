from django.contrib import admin

from .models import Vaga

class VagaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'empresa')
    list_filter = ['titulo', 'empresa']
    search_fields = ['titulo', 'empresa']

admin.site.register(Vaga, VagaAdmin)
