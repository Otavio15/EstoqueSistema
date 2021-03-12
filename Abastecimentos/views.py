from django.shortcuts import render

def vizualisar_abastecimentos(request):
    return render(request, 'vizualisar-abastecimentos.html')

def cadastrar_abastecimento(request):
    return render(request, 'cadastrar-abastecimento.html')
