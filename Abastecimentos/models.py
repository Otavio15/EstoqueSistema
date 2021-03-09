from django.db import models
from Veiculos.models import CadastrarVeiculo
# Create your models here.

##### Cadastrar Abastecimentos #####

class Posto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Posto', max_length=50)
    imagem = models.ImageField('Imagem',upload_to='img', blank=True)
    descricao = models.TextField('Descrição', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Posto'
        verbose_name_plural = 'Postos'

    def __str__(self):
        return self.nome

class Abastecimento(models.Model):
    id = models.AutoField(primary_key=True)
    veiculo = models.ForeignKey(CadastrarVeiculo,on_delete=models.PROTECT)
    data = models.DateField('Data do abastecimento')
    posto = models.ForeignKey(Posto, on_delete=models.PROTECT)
    valor_litro = models.DecimalField('Valor por litro', max_digits=10, decimal_places=2)
    valor_total = models.DecimalField('Valor total do abastecimento', max_digits=100000, decimal_places=2)
    imagem = models.ImageField('Imagem',upload_to='img', blank=True)
    descricao = models.TextField('Descrição', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Abastecimento'
        verbose_name_plural = 'Abastecimentos'

    def __str__(self):
        return str(self.veiculo)

##### Fim cadastrar Abastecimentos #####