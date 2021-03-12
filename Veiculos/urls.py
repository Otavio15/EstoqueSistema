from django.urls import path

from .views import vizualisar_veiculos

urlpatterns = [
    path('', vizualisar_veiculos, name='vizualisar_veiculos')
]
