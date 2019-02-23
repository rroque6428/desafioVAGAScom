from django.contrib import admin

from .models import Candidatura

class CandidaturaAdmin(admin.ModelAdmin):
    list_display = ('id_vaga', 'id_pessoa', 'score')
    list_filter = ['id_vaga__titulo', 'id_pessoa__nome']
    search_fields = ['id_vaga__titulo', 'id_pessoa__nome']

admin.site.register(Candidatura, CandidaturaAdmin)
