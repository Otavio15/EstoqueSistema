from django import forms
from .models import CadastrarProduto, CadastrarVeiculo, Abastecimento, Categoria, Cliente, Fabricante, Local, Manutencao, Marca, ModeloVeiculo, Posto, Produto, Requisicoes, Responsavel, TipoServico, Veiculo

class CadastrarProdutoModelForm(forms.ModelForm):
    class Meta:
        model = CadastrarProduto

class CadastrarVeiculoModelForm(forms.ModelForm):
    class Meta:
        model = CadastrarVeiculo

class AbastecimentoModelForm(forms.ModelForm):
    class Meta:
        model = Abastecimento

class CategoriaModelForm(forms.ModelForm):
    class Meta:
        model = Categoria

class ClienteModelsForm(forms.ModelForm):
    class Meta:
        model = Cliente

class FabricanteModelsForm(forms.ModelForm):
    class Meta:
        model = Fabricante

class LocalModelForm(forms.ModelForm):
    class Meta:
        model = Local

class ManutencaoModelForm(forms.ModelForm):
    class Meta:
        model = Manutencao

class MarcaModelForm(forms.ModelForm):
    class Meta:
        model = Marca

class ModeloVeiculoModelForm(forms.ModelForm):
    class Meta:
        model = ModeloVeiculo

class PostoModelForm(forms.ModelForm):
    class Meta:
        model = Posto

class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto

class RequisicoesModelForm(forms.ModelForm):
    class Meta:
        model = Requisicoes

class ResponsavelModelForm(forms.ModelForm):
    class Meta:
        model = Responsavel

class TipoServicoModelForm(forms.ModelForm):
    class Meta:
        model = TipoServico

class VeiculoModelForm(forms.ModelForm):
    class Meta:
        model = Veiculo