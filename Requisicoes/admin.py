from django.contrib import admin
from .models import Requisicoes
# Register your models here.

from django.http import HttpResponse, HttpResponseForbidden
from actions import export_as_csv_action

class RequisicoesAdmin(admin.ModelAdmin):
    search_fields = ['titulo']
    list_display = ('titulo', 'data', 'veiculo', 'local', 'created_at')
    actions = [export_as_csv_action("Exportar para CSV", fields=['titulo', 'data', 'veiculo', 'local', 'created_at'])]
    list_per_page = 250

admin.site.register(Requisicoes, RequisicoesAdmin)