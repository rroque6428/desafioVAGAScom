from django.db import models

class NivelExperiencia(models.Model):
    descricao = models.CharField(max_length=30)
    nivel = models.IntegerField()

    def __str__(self):
        return self.descricao
        
    class Meta:
        ordering = ('nivel',)
        verbose_name = 'Nivel de Experiência'
