# admin.py (ForeignKey)
from django.contrib import admin
from .models import CadastrarProduto, Cliente, CadastrarVeiculo, Produto, Categoria, Marca, Responsavel, ModeloVeiculo, Veiculo, Manutencao, Fabricante, Local, Abastecimento, Posto, UnidadeMedida, TipoServico

class TipoServicoInline(admin.TabularInline):
    model = TipoServico
    extra = 1

class ManutencaoAdmin(admin.ModelAdmin):
    list_display = ('veiculo', 'valor', 'data', 'local')
    inlines = [TipoServicoInline]

class CadastrarVeiculoAdmin(admin.ModelAdmin):
    list_display = ('modelo_veiculo', 'placa_veiculo', 'ano_veicuo')

class CadastrarProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'quantidade', 'categoria', 'marca_produto')

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

class ResponsavelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

class ModeloVeiculoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

class TipoServicoAdmin(admin.ModelAdmin):
    list_display = ('tipo_servico', 'valor')

class FabricanteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

class LocalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'descricao')

class PostoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

class AbastecimentoAdmin(admin.ModelAdmin):
    list_display = ('veiculo', 'data', 'posto', 'valor_total')


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
# Register your models here.
