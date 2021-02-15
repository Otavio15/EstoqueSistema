from django.shortcuts import render

from .models import CadastrarVeiculo

def index(request):
    veiculos = CadastrarVeiculo.objects.all()

    context = {
        'veiculos': veiculos,
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def cadastrar_veiculos(request):
    veiculos = CadastrarVeiculo.objects.all()

    context = {
        'veiculos': veiculos
    }
    
    return render(request, 'cadrastrar-veiculos.html', context)

def veiculo(request, pk):
    
    veiculo_obj =  CadastrarVeiculo.objects.get(id = pk)

    context = {
        'veiculo': veiculo_obj
    }

    return render(request, 'veiculo.html', context)