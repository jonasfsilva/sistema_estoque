from django.contrib import admin
from fornecedores.models import Fornecedor

@admin.register(Fornecedor)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'endereco', 'mais_detalhes')