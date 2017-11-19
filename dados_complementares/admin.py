from django.contrib import admin
from dados_complementares.models import UnidadeMedida

@admin.register(UnidadeMedida)
class UnidadeMedidaAdmin(admin.ModelAdmin):
    pass