from django.shortcuts import render

def index(request):
    context = {
        'curso': 'Programação Web com Django Framework',
        'curso2': 'Django'
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')



