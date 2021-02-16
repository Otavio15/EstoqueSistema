from django.db import models

class Produto(models.Model):
    nome = models.CharField('Produto', max_length=50)
    imagem = models.ImageField('Imagem',upload_to='img', blank=True)
    descricao = models.TextField('Descrição', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Categoria', max_length=50)
    imagem = models.ImageField('Imagem',upload_to='img', blank=True)
    descricao = models.TextField('Descrição', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome

class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Marca', max_length=50)
    imagem = models.ImageField('Imagem',upload_to='img', blank=True)
    descricao = models.TextField('Descrição', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.nome

class UnidadeMedida(models.Model):
    id = models.AutoField(primary_key=True)
    unidade_medida = models.CharField('Unidade de medida', max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Unidade de medida'
        verbose_name_plural = 'Unidade de medida'

    def __str__(self):
        return self.unidade_medida

class CadastrarProduto(models.Model):
    nome = models.ForeignKey(Produto, on_delete=models.CASCADE)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    quantidade = models.IntegerField('Quantidade')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca_produto = models.ForeignKey(Marca, on_delete=models.CASCADE)
    unidade_de_medida = models.ForeignKey(UnidadeMedida, on_delete=models.CASCADE)
    descricao = models.TextField('Descrição', blank=True)
    imagem = models.ImageField('Imagem',upload_to='img', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Cadastrar produto'
        verbose_name_plural = 'Cadastrar produtos'

    def __str__(self):
        return str(self.nome)
    
class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=50)
    sobre_nome = models.CharField('Sobre nome', max_length=50)
    email = models.CharField('Email', max_length=70)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome

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

    class Meta:
        verbose_name = 'Cadastrar veículo'
        verbose_name_plural = 'Cadastrar veículos'

    def __str__(self):
        return str(self.nome_veiculo) + ' -- ' + str(self.placa_veiculo)
    

class Manutencao(models.Model):
    id = models.AutoField(primary_key=True)
    veiculo = models.OneToOneField(CadastrarVeiculo,on_delete=models.PROTECT)
    valor = models.DecimalField('Valor da manutenção', max_digits=100000, decimal_places=2)
    data = models.DateField('Data da manutenção')
    local = models.OneToOneField(Local, on_delete=models.PROTECT, verbose_name='Local da manutenção')
    descricao = models.TextField('Descrição', blank=True)
    imagem = models.ImageField('Imagem',upload_to='img', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Manutenção'
        verbose_name_plural = 'Manutenções'

    def __str__(self):
        return 'Veículo: '+str(self.veiculo) +' - Valor: '+str(self.valor)+' - Local: '+str(self.local)

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
    veiculo = models.OneToOneField(CadastrarVeiculo,on_delete=models.CASCADE)
    data = models.DateField('Data do abastecimento')
    posto = models.OneToOneField(Posto, on_delete=models.CASCADE)
    valor_litro = models.DecimalField('Valor por litro', max_digits=100000, decimal_places=2)
    valor_total = models.DecimalField('Valor total do abastecimento', max_digits=100000, decimal_places=2)
    imagem = models.ImageField('Imagem',upload_to='img', blank=True)
    descricao = models.TextField('Descrição', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Abastecimento'
        verbose_name_plural = 'Abastecimentos'

    def __str__(self):
        return str(self.veiculo) + ' -- ' + str(self.data) + ' -- ' + str(self.posto)


class Requisicoes(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.TextField('Descrição', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Requisição'
        verbose_name_plural = 'Requisições'