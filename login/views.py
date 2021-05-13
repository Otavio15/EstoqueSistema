from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def login_page(request):
    return render(request, 'login.html')

@csrf_protect
def login_submit(request):
    if request.POST:
        usuario = request.POST.get('user')
        senha = request.POST.get('senha')
        user = authenticate(username=usuario, password=senha)
        print('User: {} ---------- Usuário {}, Senha {}'.format(str(user), usuario, senha))
        if user is not None:
            login(request, user)
            return redirect('/admin/')
        else:
            messages.error(request, 'Usuário ou senha inválidos')
    
    return redirect('/login/')