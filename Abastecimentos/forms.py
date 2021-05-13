from django import forms
from .models import Abastecimento, CadastrarVeiculo, Posto

class Abastecimento_ModelForm(forms.ModelForm):
    class Meta:
        model = Abastecimento

class CadastrarVeiculo_ModelForm(forms.ModelForm):
    class Meta:
        model = CadastrarVeiculo