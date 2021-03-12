from django.urls import path

from .views import vizualisar_produtos, cadastrar_produto

urlpatterns = [
    path('', vizualisar_produtos, name='vizualisar_produtos'),
    path('cadastrar/', cadastrar_produto, name='cadastrar_produto')
]
