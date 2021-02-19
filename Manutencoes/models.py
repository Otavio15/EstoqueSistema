from django.db import models

from Veiculos.models import CadastrarVeiculo
# Create your models here.

##### Cadastrar Manutencao #####

class Local(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Local', max_length=50)
    cnpj = models.CharField('CNPJ', max_length=50, blank=True)
    imagem = models.ImageField('Imagem',upload_to='img', blank=True)
    descricao = models.TextField('Descrição', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = 'Locais'

    def __str__(self):
        return self.nome
    

class Manutencao(models.Model):
    id = models.AutoField(primary_key=True)
    veiculo = models.ForeignKey(CadastrarVeiculo,on_delete=models.PROTECT)
    valor = models.DecimalField('Valor da manutenção', max_digits=100000, decimal_places=2)
    data = models.DateField('Data da manutenção')
    local = models.ForeignKey(Local, on_delete=models.PROTECT, verbose_name='Local da manutenção')
    descricao = models.TextField('Descrição', blank=True)
    imagem = models.ImageField('Imagem',upload_to='img', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Manutenção'
        verbose_name_plural = 'Manutenções'

    def __str__(self):
        return 'Veículo: '+str(self.veiculo)

class TipoServico(models.Model):
    tipo_servico = models.CharField('Serviço', max_length=50)
    valor = models.DecimalField('Valor do serviço', max_digits=100000, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    manutencao = models.ForeignKey(Manutencao, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Tipo de serviço'
        verbose_name_plural = 'Tipos de serviços'

    def __str__(self):
        return self.tipo_servico + ' - R$: '+str(self.valor)

##### Fim cadastrar manutenções #####
