from django.shortcuts import render

# Create your views here.

def vizualisar_veiculos(request):
    return render(request, 'vizualisar-veiculos.html')