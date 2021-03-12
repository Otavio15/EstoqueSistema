from django.urls import path

from .views import vizualisar_fretes

urlpatterns = [
    path('', vizualisar_fretes, name='vizualisar_fretes')
]
