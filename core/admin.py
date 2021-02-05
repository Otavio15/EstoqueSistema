from django.contrib import admin

from .models import CadastrarProduto, Cliente, CadastrarVeiculo, Produto, Categoria, Marca, Responsavel, ModeloVeiculo, Veiculo, Manutencao, Fabricante, Local, Abastecimento, Posto

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('preco', 'quantidade')


class CadastrarVeiculoAdmin(admin.ModelAdmin):
    list_display = ('modelo_veiculo', 'placa_veiculo', 'ano_veicuo')

admin.site.register(CadastrarVeiculo, CadastrarVeiculoAdmin)
admin.site.register(CadastrarProduto, ProdutoAdmin)
admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Responsavel)
admin.site.register(ModeloVeiculo)
admin.site.register(Veiculo)
admin.site.register(Manutencao)
admin.site.register(Fabricante)
admin.site.register(Local)
admin.site.register(Posto)
admin.site.register(Abastecimento)
# Register your models here.
