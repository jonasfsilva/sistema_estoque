from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=80)
    telefone = models.CharField(max_length=80)
    endereco = models.CharField(max_length=130, null=True, blank=True)
    mais_detalhes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome

class ItemFornecedor(models.Model):
    fornecedor = models.CharField(max_length=80)
    item = models.CharField(max_length=80)
    valor_unitario = models.CharField(max_length=130, null=True, blank=True)

    def __str__(self):
        return "{0}/(1)".format(self.item, self.fornecedor)