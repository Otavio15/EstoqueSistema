from django.shortcuts import render

def vizualisar_requisicoes(request):
    return render(request, 'vizualisar-requisicoes.html')

def cadastrar_requisicao(request):
    return render(request, 'cadastrar-requisicao.html')
