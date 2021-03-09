from django.db import models

# Create your models here.

class Cidades(models.Model):
    id = models.AutoField(primary_key=True)
    nome_cidade = models.CharField('Nome da cidade', max_length=50)
    cep = models.CharField('CEP', max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

    def __str__(self):
        return self.nome_cidade


class Fretes(models.Model):
    id = models.AutoField(primary_key=True)
    cidade = models.ForeignKey(Cidades, verbose_name='Cidade', on_delete=models.PROTECT)
    data = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Frete'
        verbose_name_plural = 'Fretes'

    def __str__(self):
        return self.cidade


class Mercadorias(models.Model):
    nome = models.CharField('Nome da mercadoria', max_length=50)
    quantidade = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    fretes = models.ForeignKey(Fretes, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Mercadoria'
        verbose_name_plural = 'Mercadorias'

    def __str__(self):
        return self.nome