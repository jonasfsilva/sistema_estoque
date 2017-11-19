from django.db import models
from autoslug import AutoSlugField

class UnidadeMedida(models.Model):
    class Meta:
        verbose_name_plural = 'Unidades de Medida'

    nome = models.CharField(max_length=80)
    nome_slug = AutoSlugField(populate_from='nome')
    abreviacao = models.CharField(max_length=10)

    def __str__(self):
        return self.nome

