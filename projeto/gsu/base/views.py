from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template.response import TemplateResponse
from django.contrib import  messages
from .models import Setor, Servico
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

def list_setor(request):
    setor = Setor.objects.all()
    return render(request,"home.html",{"setores":setor})

def list_servicos(request,setor_id):
    servico = Servico.objects.filter(setor__id=setor_id)
    return render(request,"servicos.html",{"servicos":servico})


def servico_pesquisa(request):
    template_name = 'produto_list.html'
    servico_list = Servico.objects.all()
    search = request.GET.get('search')
    if search:
        servico_list = servico_list.filter(descricao__icontains=search)
    context = {'servicos': servico_list}
    return render(request, template_name, context)
