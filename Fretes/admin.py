from django.contrib import admin
from .models import Cidades, Fretes, Mercadorias
# Register your models here.

from django.http import HttpResponse, HttpResponseForbidden
from actions import export_as_csv_action

class MercadoriasInline(admin.TabularInline):
    model = Mercadorias
    extra = 1

class MercadoriasAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ('nome', 'quantidade', 'created_at')
    actions = [export_as_csv_action("Exportar para CSV", fields=['nome', 'quantidade', 'created_at'])]
    list_per_page = 250

class CidadesAdmin(admin.ModelAdmin):
    search_fields = ['nome_cidade']
    list_display = ('nome_cidade', 'cep', 'created_at')
    actions = [export_as_csv_action("Exportar para CSV", fields=['nome_cidade', 'cep', 'created_at'])]
    list_per_page = 250

class FretesAdmin(admin.ModelAdmin):
    search_fields = ['cidade']
    inlines = [MercadoriasInline]
    list_display = ('cidade', 'data', 'created_at')
    actions = [export_as_csv_action("Exportar para CSV", fields=['cidade', 'data', 'created_at'])]
    list_per_page = 250

admin.site.register(Mercadorias, MercadoriasAdmin)
admin.site.register(Cidades, CidadesAdmin)
admin.site.register(Fretes, FretesAdmin)