from django.contrib import admin

from .models import CadastrarProduto, Cliente, CadastrarVeiculo, Produto, Categoria, Marca

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('preco', 'quantidade')


class CadastrarVeiculoAdmin(admin.ModelAdmin):
    list_display = ('modelo_veiculo', 'placa_veiculo', 'ano_veicuo')

admin.site.register(CadastrarVeiculo, CadastrarVeiculoAdmin)
admin.site.register(CadastrarProduto, ProdutoAdmin)
admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Marca)
# Register your models here.
