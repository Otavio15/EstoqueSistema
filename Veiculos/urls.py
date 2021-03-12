from django.urls import path

from .views import vizualisar_veiculos, cadastrar_veiculo

urlpatterns = [
    path('', vizualisar_veiculos, name='vizualisar_veiculos'),
    path('cadastrar/', cadastrar_veiculo, name='cadastrar_veiculo')
]
