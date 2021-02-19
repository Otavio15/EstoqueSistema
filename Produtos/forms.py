from django import forms
from .models import CadastrarProduto, CadastrarVeiculo, Abastecimento, Categoria, Cliente, Fabricante, Local, Manutencao, Marca, ModeloVeiculo, Posto, Produto, Requisicoes, Responsavel, TipoServico, Veiculo

class CadastrarProdutoModelForm(forms.ModelForm):
    class Meta:
        model = CadastrarProduto
        fields = ['nome','preco', 'quantidade', 'categoria', 'marca_produto', 'unidade_de_medida', 'descricao', 'imagem', 'created_at', 'update_at']

class CadastrarVeiculoModelForm(forms.ModelForm):
    class Meta:
        model = CadastrarVeiculo
        fields = ['id','nome_veiculo', 'modelo_veiculo', 'placa_veiculo', 'ano_veicuo', 'fabricante_veiculo', 'responsavel', 'tipo', 'descricao', 'imagem', 'created_at', 'update_at']

class AbastecimentoModelForm(forms.ModelForm):
    class Meta:
        fields = ['id','veiculo', 'data', 'posto', 'valor_litro', 'valor_total', 'imagem', 'descricao', 'created_at', 'update_at']
        model = Abastecimento

class CategoriaModelForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['id','nome', 'imagem', 'descricao', 'created_at', 'update_at']

class ClienteModelForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome','sobre_nome', 'email']

class FabricanteModelForm(forms.ModelForm):
    class Meta:
        model = Fabricante
        fields = ['id','nome', 'imagem', 'descricao', 'created_at', 'update_at']

class LocalModelForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = ['nome','cnpj', 'imagem', 'descricao', 'created_at', 'update_at']

class ManutencaoModelForm(forms.ModelForm):
    class Meta:
        model = Manutencao
        fields = ['id','veiculo', 'valor', 'data', 'local', 'tipo_servico', 'descricao', 'imagem', 'created_at', 'update_at']

class MarcaModelForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['id','nome', 'imagem', 'descricao', 'created_at', 'update_at']

class ModeloVeiculoModelForm(forms.ModelForm):
    class Meta:
        model = ModeloVeiculo
        fields = ['id','nome', 'imagem', 'descricao', 'created_at', 'update_at']

class PostoModelForm(forms.ModelForm):
    class Meta:
        fields = ['id','nome', 'imagem', 'descricao', 'created_at', 'update_at']
        model = Posto

class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome','imagem', 'descricao', 'created_at', 'update_at']

class RequisicoesModelForm(forms.ModelForm):
    class Meta:
        fields = ['id','descricao', 'created_at', 'update_at']
        model = Requisicoes

class ResponsavelModelForm(forms.ModelForm):
    class Meta:
        fields = ['id','nome', 'imagem', 'descricao']
        model = Responsavel

class TipoServicoModelForm(forms.ModelForm):
    class Meta:
        model = TipoServico
        fields = ['id','tipo_servico', 'valor', 'descricao', 'created_at', 'update_at']

class VeiculoModelForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['id','nome', 'imagem', 'descricao', 'created_at', 'update_at']