from django.urls import path

from .views import vizualisar_requisicoes

urlpatterns = [
    path('', vizualisar_requisicoes, name='vizualisar_requisicoes')
]
