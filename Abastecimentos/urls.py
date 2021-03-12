
from django.urls import path

from .views import vizualisar_abastecimentos

urlpatterns = [
    path('', vizualisar_abastecimentos, name='vizualisar_abastecimentos')
]
