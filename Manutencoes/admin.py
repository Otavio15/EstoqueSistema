from django.contrib import admin
from .models import TipoServico, Local, Manutencao
# Register your models here.
from django.http import HttpResponse, HttpResponseForbidden
from actions import export_as_csv_action

class TipoServicoInline(admin.TabularInline):
    model = TipoServico
    extra = 1

class TipoServicoAdmin(admin.ModelAdmin):
    search_fields = ['tipo_servico']
    list_display = ('tipo_servico', 'valor', 'created_at')
    actions = [export_as_csv_action("Exportar para CSV", fields=['tipo_servico', 'valor', 'created_at'])]
    list_per_page = 250

class ManutencaoAdmin(admin.ModelAdmin):
    list_display = ('veiculo', 'valor', 'data', 'local', 'created_at')
    search_fields = ['veiculo']
    inlines = [TipoServicoInline]
    actions = [export_as_csv_action("Exportar para CSV", fields=['veiculo', 'valor', 'data', 'local', 'created_at'])]
    list_per_page = 250

class LocalAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ('nome', 'cnpj', 'descricao', 'created_at')
    actions = [export_as_csv_action("Exportar para CSV", fields=['nome', 'cnpj', 'descricao', 'created_at'])]
    list_per_page = 250

admin.site.register(Manutencao, ManutencaoAdmin)
admin.site.register(TipoServico, TipoServicoAdmin)
admin.site.register(Local, LocalAdmin)