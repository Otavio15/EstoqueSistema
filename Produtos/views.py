from django.shortcuts import render

def vizualisar_produtos(request):
    return render(request, 'vizualisar-produtos.html')