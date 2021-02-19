from django.contrib import admin
from .models import Abastecimento, Posto

from django.http import HttpResponse, HttpResponseForbidden
from actions import export_as_csv_action
# Register your models here.

class AbastecimentoAdmin(admin.ModelAdmin):
    search_fields = ['veiculo']
    list_display = ('veiculo', 'data', 'posto', 'valor_total', 'created_at')
    actions = [export_as_csv_action("Exportar para CSV", fields=['veiculo', 'data', 'posto', 'valor_total', 'created_at'])]
    list_per_page = 250

class PostoAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ('nome', 'descricao', 'created_at')
    actions = [export_as_csv_action("Exportar para CSV", fields=['nome', 'descricao', 'created_at'])]
    list_per_page = 250

admin.site.register(Abastecimento, AbastecimentoAdmin)
admin.site.register(Posto, PostoAdmin)