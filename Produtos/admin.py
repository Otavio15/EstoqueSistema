# admin.py (ForeignKey)
from django.contrib import admin
from .models import CadastrarProduto, Produto, Categoria, Marca, UnidadeMedida

from django.http import HttpResponse, HttpResponseForbidden
from actions import export_as_csv_action

class CadastrarProdutoAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ('nome', 'preco', 'quantidade', 'categoria', 'marca_produto', 'created_at')
    actions = [export_as_csv_action("Exportar para CSV", fields=['nome', 'preco', 'quantidade', 'categoria', 'marca_produto', 'created_at'])]
    list_per_page = 250

class ProdutoAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ('nome', 'descricao', 'created_at')
    actions = [export_as_csv_action("Exportar para CSV", fields=['nome', 'descricao', 'created_at'])]
    list_per_page = 250

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ('nome', 'descricao', 'created_at')
    actions = [export_as_csv_action("Exportar para CSV", fields=['nome', 'descricao', 'created_at'])]
    list_per_page = 250

class MarcaAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ('nome', 'descricao', 'created_at')
    actions = [export_as_csv_action("Exportar para CSV", fields=['nome', 'descricao', 'created_at'])]
    list_per_page = 250

class UnidadeMedidaAdmin(admin.ModelAdmin):
    search_fields = ['unidade_medida']
    list_display = ('unidade_medida', 'created_at')
    actions = [export_as_csv_action("Exportar para CSV", fields=['unidade_medida', 'created_at'])]
    list_per_page = 250


admin.site.register(CadastrarProduto, CadastrarProdutoAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(UnidadeMedida, UnidadeMedidaAdmin)


admin.site.index_title = "Bem vindo ao sistema de gestão interna da Nippontec."

# Register your models here.
