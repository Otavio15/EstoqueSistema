from django.shortcuts import render

def vizualisar_produtos(request):
    return render(request, 'vizualisar-produtos.html')

def cadastrar_produto(request):
    return render(request, 'cadastrar-produto.html')