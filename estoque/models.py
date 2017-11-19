from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from dados_complementares.models import UnidadeMedida

class Item(models.Model):
    class Meta:
        verbose_name_plural = 'Itens do Estoque'

    nome = models.CharField(max_length=80)
    nome_slug = AutoSlugField(populate_from='nome')
    descricao = models.TextField(null=True, blank=True)
    valor_unit = models.FloatField(verbose_name='Valor Unitario')

    def __str__(self):
        return self.nome


class MovimentacaoEstoque(models.Model):
    class Meta:
        verbose_name_plural = 'Movimentações de Estoque'

    CHOICES = (
        (True, 'Entrada'),
        (False, 'Saida')
    )

    item = models.ForeignKey(Item)
    quantidade = models.PositiveIntegerField()
    medida = models.ForeignKey(UnidadeMedida)
    fluxo = models.BooleanField(choices=CHOICES)
    data_informada = models.DateField(verbose_name='Data compra')
    data_do_registro = models.DateTimeField(auto_now_add=True)
    usuario_responsavel = models.ForeignKey(User)

    def __str__(self):
        return "{0} - Qtd:{1} {2}".format(self.item, self.quantidade, self.fluxo)
