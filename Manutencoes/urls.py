from django.urls import path

from .views import vizualisar_manutencoes

urlpatterns = [
    path('', vizualisar_manutencoes, name='vizualisar_manutencoes')
]
