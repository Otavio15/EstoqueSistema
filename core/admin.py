# admin.py (ForeignKey)
from django.contrib import admin
from .models import CadastrarProduto, Cliente, CadastrarVeiculo, Produto, Categoria, Marca, Responsavel, ModeloVeiculo, Veiculo, Manutencao, Fabricante, Local, Abastecimento, Posto, UnidadeMedida, TipoServico

class TipoServicoInline(admin.TabularInline):
    model = TipoServico
    extra = 1

class ManutencaoAdmin(admin.ModelAdmin):
    inlines = [TipoServicoInline]

class CadastrarVeiculoAdmin(admin.ModelAdmin):
    list_display = ('modelo_veiculo', 'placa_veiculo', 'ano_veicuo')


admin.site.register(CadastrarVeiculo, CadastrarVeiculoAdmin)
admin.site.register(CadastrarProduto)
admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Responsavel)
admin.site.register(ModeloVeiculo)
admin.site.register(Veiculo)
admin.site.register(Manutencao, ManutencaoAdmin)
admin.site.register(TipoServico)
admin.site.register(Fabricante)
admin.site.register(Local)
admin.site.register(Posto)
admin.site.register(Abastecimento)
admin.site.register(UnidadeMedida)
# Register your models here.
