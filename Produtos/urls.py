from django.urls import path

from .views import vizualisar_produtos

urlpatterns = [
    path('', vizualisar_produtos, name='vizualisar_produtos')
]
