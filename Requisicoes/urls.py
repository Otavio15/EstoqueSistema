from django.urls import path

from .views import vizualisar_requisicoes, cadastrar_requisicao

urlpatterns = [
    path('', vizualisar_requisicoes, name='vizualisar_requisicoes'),
    path('cadastrar/', cadastrar_requisicao, name='cadastrar_requisicao')
]
