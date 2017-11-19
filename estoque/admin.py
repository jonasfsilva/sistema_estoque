from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from estoque.models import Item
from estoque.models import MovimentacaoEstoque


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'valor_unit')


@admin.register(MovimentacaoEstoque)
class MovimentacaoEstoqueAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantidade', 'medida', 'fluxo', 'data_informada', 'usuario_responsavel')


admin.site.unregister(Group)
