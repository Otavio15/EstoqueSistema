from django.shortcuts import render

# Create your views here.

def vizualisar_manutencoes(request):
    return render(request, 'vizualisar-manutencoes.html')

def cadastrar_manutencoes(request):
    return render(request, 'cadastrar-manutencao.html')