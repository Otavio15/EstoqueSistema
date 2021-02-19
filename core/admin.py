# admin.py (ForeignKey)
from django.contrib import admin
from .models import CadastrarProduto, Cliente, CadastrarVeiculo, Produto, Categoria, Marca, Responsavel, ModeloVeiculo, Veiculo, Manutencao, Fabricante, Local, Abastecimento, Posto, UnidadeMedida, TipoServico

from django.http import HttpResponse, HttpResponseForbidden
from .actions import export_as_csv_action

class TipoServicoInline(admin.TabularInline):
    model = TipoServico
    extra = 1

class ManutencaoAdmin(admin.ModelAdmin):
    list_display = ('veiculo', 'valor', 'data', 'local')
    search_fields = ['veiculo']
    inlines = [TipoServicoInline]
    actions = [export_as_csv_action("Exportar para CSV", fields=['veiculo', 'valor', 'data', 'local'])]
    list_per_page = 250

class CadastrarVeiculoAdmin(admin.ModelAdmin):
    search_fields = ['placa_veiculo']
    list_display = ('placa_veiculo', 'modelo_veiculo', 'ano_veicuo')
    actions = [export_as_csv_action("Exportar para CSV", fields=['placa_veiculo', 'modelo_veiculo', 'ano_veicuo'])]
    list_per_page = 250

class CadastrarProdutoAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ('nome', 'preco', 'quantidade', 'categoria', 'marca_produto')
    actions = [export_as_csv_action("Exportar para CSV", fields=['nome', 'preco', 'quantidade', 'categoria', 'marca_produto'])]
    list_per_page = 250

class ProdutoAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ('nome', 'descricao')
    actions = [export_as_csv_action("Exportar para CSV", fields=['nome', 'descricao'])]
    list_per_page = 250

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ('nome', 'descricao')
    actions = [export_as_csv_action("Exportar para CSV", fields=['nome', 'descricao'])]
    list_per_page = 250

class MarcaAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ('nome', 'descricao')
    actions = [export_as_csv_action("Exportar para CSV", fields=['nome', 'descricao'])]
    list_per_page = 250

class ResponsavelAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ('nome', 'descricao')
    actions = [export_as_csv_action("Exportar para CSV", fields=['nome', 'descricao'])]
    list_per_page = 250

class ModeloVeiculoAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ('nome', 'descricao')
    actions = [export_as_csv_action("Exportar para CSV", fields=['nome', 'descricao'])]
    list_per_page = 250

class VeiculoAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ('nome', 'descricao')
    actions = [export_as_csv_action("Exportar para CSV", fields=['nome', 'descricao'])]
    list_per_page = 250

class TipoServicoAdmin(admin.ModelAdmin):
    search_fields = ['tipo_servico']
    list_display = ('tipo_servico', 'valor')
    actions = [export_as_csv_action("Exportar para CSV", fields=['tipo_servico', 'valor'])]
    list_per_page = 250

class FabricanteAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ('nome', 'descricao')
    actions = [export_as_csv_action("Exportar para CSV", fields=['nome', 'descricao'])]
    list_per_page = 250

class LocalAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ('nome', 'cnpj', 'descricao')
    actions = [export_as_csv_action("Exportar para CSV", fields=['nome', 'cnpj', 'descricao'])]
    list_per_page = 250

class PostoAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ('nome', 'descricao')
    actions = [export_as_csv_action("Exportar para CSV", fields=['nome', 'descricao'])]
    list_per_page = 250

class AbastecimentoAdmin(admin.ModelAdmin):
    search_fields = ['veiculo']
    list_display = ('veiculo', 'data', 'posto', 'valor_total')
    actions = [export_as_csv_action("Exportar para CSV", fields=['veiculo', 'data', 'posto', 'valor_total'])]
    list_per_page = 250

admin.site.register(CadastrarVeiculo, CadastrarVeiculoAdmin)
admin.site.register(CadastrarProduto, CadastrarProdutoAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Responsavel, ResponsavelAdmin)
admin.site.register(ModeloVeiculo, ModeloVeiculoAdmin)
admin.site.register(Veiculo, VeiculoAdmin)
admin.site.register(Manutencao, ManutencaoAdmin)
admin.site.register(TipoServico, TipoServicoAdmin)
admin.site.register(Fabricante, FabricanteAdmin)
admin.site.register(Local, LocalAdmin)
admin.site.register(Posto, PostoAdmin)
admin.site.register(Abastecimento, AbastecimentoAdmin)
admin.site.register(UnidadeMedida)

admin.site.index_title = "Bem vindo ao sistema de controle de estoque da Nippontec."

# Register your models here.
