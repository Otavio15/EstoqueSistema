from django.urls import path

from .views import vizualisar_manutencoes, cadastrar_manutencoes

urlpatterns = [
    path('', vizualisar_manutencoes, name='vizualisar_manutencoes'),
    path('cadastrar/', cadastrar_manutencoes, name='cadastrar_manutencao')
]
