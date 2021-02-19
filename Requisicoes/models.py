from django.db import models
from tinymce import HTMLField

from Veiculos.models import Veiculo
from Manutencoes.models import Local

# Create your models here.
class Requisicoes(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Título da requisição', max_length=50)
    data = models.DateField('Data da requisição')
    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT)
    local = models.ForeignKey(Local, on_delete=models.PROTECT, verbose_name='Local do abastecimento')
    requisicao = HTMLField('Requisição')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Requisição'
        verbose_name_plural = 'Requisições'

    def __str__(self):
        return str(self.titulo)