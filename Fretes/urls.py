from django.urls import path

from .views import vizualisar_fretes, cadastrar_frete

urlpatterns = [
    path('', vizualisar_fretes, name='vizualisar_fretes'),
    path('cadastrar/', cadastrar_frete, name='cadastrar_frete')
]
