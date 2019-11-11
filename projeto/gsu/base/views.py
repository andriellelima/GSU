from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template.response import TemplateResponse
from django.contrib import  messages
# Create your views here.

def home(request):
    return render(request,'home.html')


def logar(request):
    if request.user.is_authenticated:
        return render(request,'teste.html')
    if request.method == 'POST':
        usuario = request.POST['usuario']
        #usuario = usuario.replace('.','').replace('-','')
        senha = request.POST['senha']
        user = authenticate(username=usuario, password=senha)
        if user is not None:
            if user.is_active:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                return render(request,'teste.html')
            else:
                messages.error(request, 'Usuário inativo')
        else:
            messages.error(request, 'CPF ou senha inválidos!')
    return render(request, 'login.html', locals())


def setor(request):
    return render(request,'proaes.html')

def sair(request):
    logout(request)
    return redirect('logar')
