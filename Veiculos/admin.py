from django.contrib import admin
from .models import CadastrarVeiculo, Fabricante, ModeloVeiculo, Responsavel, Veiculo
# Register your models here.
from django.http import HttpResponse, HttpResponseForbidden
from actions import export_as_csv_action

class CadastrarVeiculoAdmin(admin.ModelAdmin):
    search_fields = ['placa_veiculo']
    list_display = ('placa_veiculo', 'modelo_veiculo', 'ano_veicuo', 'created_at')
    actions = [export_as_csv_action("Exportar para CSV", fields=['placa_veiculo', 'modelo_veiculo', 'ano_veicuo', 'created_at'])]
    list_per_page = 250

class ModeloVeiculoAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ('nome', 'descricao', 'created_at')
    actions = [export_as_csv_action("Exportar para CSV", fields=['nome', 'descricao', 'created_at'])]
    list_per_page = 250

class VeiculoAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ('nome', 'descricao')
    actions = [export_as_csv_action("Exportar para CSV", fields=['nome', 'descricao', 'created_at'])]
    list_per_page = 250

class FabricanteAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ('nome', 'descricao', 'created_at')
    actions = [export_as_csv_action("Exportar para CSV", fields=['nome', 'descricao', 'created_at'])]
    list_per_page = 250

class ResponsavelAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ('nome', 'descricao', 'created_at')
    actions = [export_as_csv_action("Exportar para CSV", fields=['nome', 'descricao', 'created_at'])]
    list_per_page = 250

admin.site.register(CadastrarVeiculo, CadastrarVeiculoAdmin)
admin.site.register(Veiculo, VeiculoAdmin)
admin.site.register(ModeloVeiculo, ModeloVeiculoAdmin)
admin.site.register(Fabricante, FabricanteAdmin)
admin.site.register(Responsavel, ResponsavelAdmin)