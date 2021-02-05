from django.db import models

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Produto', max_length=50)
    imagem = models.ImageField('Imagem',upload_to='img', blank=True)
    descricao = models.TextField('Descrição', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Categoria', max_length=50)
    imagem = models.ImageField('Imagem',upload_to='img', blank=True)
    descricao = models.TextField('Descrição', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Marca', max_length=50)
    imagem = models.ImageField('Imagem',upload_to='img', blank=True)
    descricao = models.TextField('Descrição', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class CadastrarProduto(models.Model):
    nome = models.OneToOneField(Produto, on_delete=models.CASCADE)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    quantidade = models.IntegerField('Quantidade')
    categoria = models.OneToOneField(Categoria, on_delete=models.CASCADE)
    marca_produto = models.OneToOneField(Marca, on_delete=models.CASCADE)
    unidade_de_medida = models.CharField('Unidade de medida', max_length=5)
    descricao = models.TextField('Descrição', blank=True)
    imagem = models.ImageField('Imagem',upload_to='img', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.nome)
    
class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=50)
    sobre_nome = models.CharField('Sobre nome', max_length=50)
    email = models.CharField('Email', max_length=70)

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Veiculo', max_length=50)
    imagem = models.ImageField('Imagem',upload_to='img', blank=True)
    descricao = models.TextField('Descrição', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Fabricante(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Fabricante', max_length=50)
    imagem = models.ImageField('Imagem',upload_to='img', blank=True)
    descricao = models.TextField('Descrição', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class ModeloVeiculo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Modelo do veículo', max_length=50)
    imagem = models.ImageField('Imagem',upload_to='img', blank=True)
    descricao = models.TextField('Descrição', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Responsavel(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Responsável', max_length=50)
    imagem = models.ImageField('Imagem',upload_to='img', blank=True)
    descricao = models.TextField('Descrição', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Local(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Local', max_length=50)
    cnpj = models.CharField('CNPJ', max_length=50, blank=True)
    imagem = models.ImageField('Imagem',upload_to='img', blank=True)
    descricao = models.TextField('Descrição', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class CadastrarVeiculo(models.Model):
    id = models.AutoField(primary_key=True)
    nome_veiculo = models.OneToOneField(Veiculo, on_delete=models.CASCADE)
    modelo_veiculo = models.OneToOneField(ModeloVeiculo, on_delete=models.CASCADE)
    placa_veiculo = models.CharField('Placa do veículo', max_length=10)
    ano_veicuo = models.IntegerField('Ano do veículo')
    fabricante_veiculo = models.OneToOneField(Fabricante, on_delete=models.CASCADE)
    responsavel = models.OneToOneField(Responsavel, on_delete=models.CASCADE)
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

    def __str__(self):
        return str(self.nome_veiculo) + ' -- ' + str(self.placa_veiculo)

class Manutencao(models.Model):
    id = models.AutoField(primary_key=True)
    veiculo = models.OneToOneField(CadastrarVeiculo,on_delete=models.CASCADE)
    valor = models.DecimalField('Valor da manutenção', max_digits=100000, decimal_places=4)
    data = models.DateField('Data da manutenção')
    local = models.OneToOneField(Local, on_delete=models.CASCADE, verbose_name='Local da manutenção')
    descricao = models.TextField('Descrição', blank=True)
    imagem = models.ImageField('Imagem',upload_to='img', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Veículo: '+str(self.veiculo) +' - Valor: '+str(self.valor)+' - Responsável: '+str(self.responsavel)