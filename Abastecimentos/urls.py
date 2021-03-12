
from django.urls import path

from .views import vizualisar_abastecimentos, cadastrar_abastecimento

urlpatterns = [
    path('', vizualisar_abastecimentos, name='vizualisar_abastecimentos'),
    path('cadastrar/', cadastrar_abastecimento, name='cadastrar_abastecimentos')
]
