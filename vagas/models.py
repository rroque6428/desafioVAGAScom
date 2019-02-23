from django.db import models

from nivelexperiencia.models import NivelExperiencia

class Vaga(models.Model):
    empresa = models.CharField(max_length=100)
    titulo = models.CharField(max_length=80)
    descricao = models.TextField()
    localizacao = models.CharField(max_length=1)
    nivel = models.IntegerField()
    # nivel = models.ForeignKey(NivelExperiencia, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo

