from django.shortcuts import render

def vizualisar_fretes(request):
    return render(request, 'vizualisar-fretes.html')

def cadastrar_frete(request):
    return render(request, 'cadastrar-frete.html')