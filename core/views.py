from django.shortcuts import render

from .models import CadastrarVeiculo

def index(request):
    context = {
        'curso': 'Programação Web com Django Framework',
        'curso2': 'Django'
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def cadastrar_veiculos(request):
    veiculos = CadastrarVeiculo.objects.all()

    contexto = {
        'veiculos': veiculos
    }
    
    return render(request, 'cadrastrar-veiculos.html', contexto)

