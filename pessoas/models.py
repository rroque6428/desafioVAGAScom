from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    profissao = models.CharField(max_length=80)
    localizacao = models.CharField(max_length=1)
    nivel = models.IntegerField()

    def __str__(self):
        return self.nome
