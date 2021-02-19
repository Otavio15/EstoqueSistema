from django.db import models
from tinymce import HTMLField

##### Cadastrar veículo #####

class Veiculo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Veiculo', max_length=50)
    imagem = models.ImageField('Imagem',upload_to='img', blank=True)
    descricao = models.TextField('Descrição', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'

    def __str__(self):
        return self.nome

class ModeloVeiculo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Modelo do veículo', max_length=50)
    imagem = models.ImageField('Imagem',upload_to='img', blank=True)
    descricao = models.TextField('Descrição', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Modelo do veículo'
        verbose_name_plural = 'Modelos dos veículos'

    def __str__(self):
        return self.nome

class Fabricante(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Fabricante', max_length=50)
    imagem = models.ImageField('Imagem',upload_to='img', blank=True)
    descricao = models.TextField('Descrição', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Fabricante'
        verbose_name_plural = 'Fabricantes'

    def __str__(self):
        return self.nome

class Responsavel(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Responsável', max_length=50)
    imagem = models.ImageField('Imagem',upload_to='img', blank=True)
    descricao = models.TextField('Descrição', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Responsável'
        verbose_name_plural = 'Responsáveis'

    def __str__(self):
        return self.nome

class CadastrarVeiculo(models.Model):
    id = models.AutoField(primary_key=True)
    nome_veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT)
    modelo_veiculo = models.ForeignKey(ModeloVeiculo, on_delete=models.PROTECT)
    placa_veiculo = models.CharField('Placa do veículo', max_length=10)
    ano_veicuo = models.IntegerField('Ano do veículo')
    fabricante_veiculo = models.ForeignKey(Fabricante, on_delete=models.PROTECT)
    responsavel = models.ForeignKey(Responsavel, on_delete=models.PROTECT, blank=True)
    tipo = models.CharField('Tipo', max_length=10, default='LEVE', blank=False, null=False,
    choices = (
        ('LEVE','LEVE'),
        ('MÉDIO', 'MÉDIO'),
        ('PESADO','PESADO')
    ))
    descricao = models.TextField('Descrição', blank=True)
    imagem = models.ImageField('Imagem',upload_to='img', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Cadastrar veículo'
        verbose_name_plural = 'Cadastrar veículos'

    def __str__(self):
        return str(self.nome_veiculo) + ' <  > ' + str(self.placa_veiculo)

##### fim cadastrar veículo #####