from django.db import models

from vagas.models import Vaga
from pessoas.models import Pessoa

class Candidatura(models.Model):
    id_vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    id_pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    score = models.IntegerField(default=-1)
